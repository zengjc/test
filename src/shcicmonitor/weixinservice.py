# -*- coding: UTF-8 -*-
'''
Created on 2015年5月11日
edited on 2015-05-12
@author: zjc
'''
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import datetime
import time
import hashlib
import xml.etree.ElementTree as ET
import threading
import tools
import jobww
RESPONSE_TEXT_TEMPLATE = '''
<xml>
<ToUserName><![CDATA[{TO_USER}]]></ToUserName>
<FromUserName><![CDATA[{FROM_USER}]]></FromUserName>
<CreateTime>{TIME_STEMP}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{RESPONSE_CONTENT}]]></Content>
</xml>
'''
# MYURL_STG = 'http://zengjc.eicp.net'
# MYURL_PRD = 'http://218.242.60.232'

TOKEN = tools.readconfig('weixin', 'TOKEN')
SPECIAL_CMD = tools.readconfig('weixin', 'SPECIAL_CMD')
SPECIAL_USERID = tools.readconfig('weixin', 'SPECIAL_USERID')
MONITOR_CMD = tools.readconfig('weixin', 'MONITOR_CMD')
# 命令最低间隔时间(秒)
INTERVALTIME = int(tools.readconfig('weixin', 'INTERVALTIME'))
# 最后一次执行命令的时间,在每次执行成功命令后更新
LASTDONETIME = datetime.datetime.now()
MONITOR_RESULT = None

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print (threading.currentThread().getName())
        print (self.path)
        text = 'This is a webservice for weixin!\n'
        if self.verifyWeixinHeader():
            if self.path.startswith('/update?'):
                #update_function_module()
                text = 'updated'
            elif self.path.startswith('/updatelocal?'):
                #update_function_module('local')
                text = 'updated'                
            else:
                text = self.receivedParams['echostr']
        self.sendResponse(text.encode())
        tools.writeLog('接收到get请求！')
        return

    def do_POST(self):
        if not self.verifyWeixinHeader():
            return
        data = self.rfile.read(int(self.headers['content-length']))
        tools.writeLog('data = ' + str(data))
        self.send_response(200)
        self.end_headers()

        worker = msgHandler(data)
        self.wfile.write(worker.response().encode('UTF-8'))

    def verifyWeixinHeader(self):
        self.receivedParams = self.requestGet()
        tools.writeLog('接受到的参数为：' + str(self.receivedParams))
        return (self.receivedParams and self.isWeixinSignature())

    def isWeixinSignature(self):
        signature = self.receivedParams['signature']
        timestamp = self.receivedParams['timestamp']
        nonce = self.receivedParams['nonce']
        # 都需要加上encode
        wishSignature = self.localSignature(TOKEN.encode(encoding='utf_8'), timestamp.encode(encoding='utf_8'), nonce.encode(encoding='utf_8'))
        return signature == wishSignature

    def localSignature(self, token, timestamp, nonce):
        items = [token, timestamp, nonce]
        items.sort()
        sha1 = hashlib.sha1()
        list(map(sha1.update, items))  #
        hashcode = sha1.hexdigest()
        return hashcode

    def requestGet(self):
        paramDict = {}
        pathParts = self.path.split('?', 1)
        if len(pathParts) < 2: return paramDict
        get_str = pathParts[1]
        if not get_str: return paramDict
        parameters = get_str.split('&')
        for param in parameters:
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            paramDict[key] = value
        return paramDict
    
    def sendResponse(self, text):
        self.send_head(str(text).encode())
        self.wfile.write(text)
        self.wfile.close()
    
    def send_head(self, text):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        fullLength = len(text)
        tools.writeLog('fullLength, text = ' + str(fullLength) + str(text))
        self.send_header("Content-Length", str(fullLength))
        self.end_headers()
        return

class msgHandler:
    def __init__(self, data):
        self.data = data
        self.dict = self._xmlToDict(self.data)
#         if self.dict['MsgType'] == 'event':
#             self.worker = eventHandler(self.dict['FromUserName'],self.dict['Event'])

    def response(self):
        responseDict = self.responseDict()
        text = self.responseXML(responseDict)
        return text
    
    
    def _xmlToDict(self, xmlText):
        xmlDict = {}
        itemlist = ET.fromstring(xmlText)
        for child in itemlist:
            xmlDict[child.tag] = child.text
        tools.writeLog('xmlDict = ' + str(xmlDict))
        return xmlDict
    
    def responseXML(self, dataDict):
        if dataDict:
            text = RESPONSE_TEXT_TEMPLATE 
            for key, value in list(dataDict.items()):
                parameter = '{%s}' % key
                text = text.replace(parameter, value)
            tools.writeLog('自己构建的返回信息：' + str(text))
        else:
            text = ''
        return text
    
    def responseDict(self):
        responseDict = {}
        try:
            responseDict['TO_USER'] = self.dict['FromUserName']
            responseDict['FROM_USER'] = self.dict['ToUserName']
            # 如果特定用户发送特定指令，那么就执行特定命令
            responseDict['RESPONSE_CONTENT'] = verifycommond(self.dict['FromUserName'], self.dict['Content'])
            responseDict['TIME_STEMP'] = str(unixTimeStamp())
            
        except:
            pass
        return responseDict

class eventHandler:
    MSG_WELCOME = '欢迎您关注我，这里是信息中心监控平台！'
    def __init__(self, user, event):
        if event == 'subscribe':
            self.response = self.MSG_WELCOME

def unixTimeStamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))

def verifycommond(fromuserid , usercommond):
    '''
    校验发送命令的用户ID和命令，根据命令执行相对于的job
    返回：查询结果 string类型
    '''
    global MONITOR_RESULT
    tools.writeLog('收到来自用户' + fromuserid + '的命令：' + usercommond)
    if usercommond == SPECIAL_CMD and '[' + fromuserid + ']' in SPECIAL_USERID:
        #执行实时查询命令
        MONITOR_RESULT = domyjob()
        return MONITOR_RESULT
    elif usercommond == MONITOR_CMD :
        print ('在这里！')
        #如果从未执行过，则执行一次，并一直返回该结果
        if MONITOR_RESULT == None or '系统运行状态'not in MONITOR_RESULT:
            MONITOR_RESULT = domyjob()
        return MONITOR_RESULT
    elif usercommond == '?':
        return '输入以下命令查询结果：监控结果'
    else:
        return '八哥学语：' + usercommond

def domyjob():
    '''
    调度后台查询任务，开始干活
    返回：查询结果 string类型
    '''
    global LASTDONETIME
    # 检查命令间隔时间，如果过于频繁，将不执行命令
    if datetime.datetime.now() >= LASTDONETIME + datetime.timedelta(seconds=INTERVALTIME):
        tools.writeLog('收到命令，开始干活！')
        LASTDONETIME = datetime.datetime.now()
        return jobww.dojobww()
    else:
        tools.writeLog('收到命令过于频繁，停止干活！')
        return '抱歉，查询过于频繁，请稍等！'
    
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    
if __name__ == '__main__':
    serverPort = 80
    server_address = ('', serverPort) 
        
    server = ThreadedHTTPServer(server_address, Handler)
    print ('weixin server is running at http://127.0.0.1:' + str(serverPort))
    server.serve_forever()

