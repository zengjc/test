# -*- coding: UTF-8 -*-
'''
Created on 2015年5月11日

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

RESPONSE_TEXT_TEMPLATE = '''
<xml>
<ToUserName><![CDATA[{TO_USER}]]></ToUserName>
<FromUserName><![CDATA[{FROM_USER}]]></FromUserName>
<CreateTime>{TIME_STEMP}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{RESPONSE_CONTENT}]]></Content>
</xml>
'''  
MYURL_STG = 'http://zengjc.eicp.net'
MYURL_PRD = 'http://218.242.60.232'
TOKEN = 'zengjingchao_office_stg1'


class Handler( BaseHTTPRequestHandler ):

    def do_GET(self):
        print (threading.currentThread().getName())
        print (self.path)
        text = 'This is a webservice for weixin!\n'
        if self.verifyWeixinHeader():
            if self.path.startswith('/update?'):
#                 update_function_module()
                text = 'updated'
            elif self.path.startswith('/updatelocal?'):
#                 update_function_module('local')
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
        #都需要加上encode
        wishSignature = self.localSignature(TOKEN.encode(encoding='utf_8'), timestamp.encode(encoding='utf_8'), nonce.encode(encoding='utf_8'))
        #print ('后面俩一致才行：' + signature + '||' + wishSignature)
        return signature == wishSignature

    def localSignature(self, token, timestamp, nonce):
        items = [token, timestamp, nonce]
        items.sort()
        sha1 = hashlib.sha1()
        list(map(sha1.update,items))#
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
        tools.writeLog('fullLength, text = ' + str(fullLength) +  str(text))
        self.send_header("Content-Length", str(fullLength))
        self.end_headers()
        return

class msgHandler:
    def __init__(self, data):
        self.data = data
        self.dict = self._xmlToDict(self.data)

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
            responseDict['RESPONSE_CONTENT'] = '八哥学语：' + self.dict['Content']
            responseDict['TO_USER'] = self.dict['FromUserName']
            responseDict['FROM_USER'] = self.dict['ToUserName']
            responseDict['TIME_STEMP'] = str(unixTimeStamp())
        except:
            pass
        return responseDict

def unixTimeStamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    
if __name__ == '__main__':
    serverPort = 80
    server_address = ('', serverPort) 
        
    server = ThreadedHTTPServer( server_address, Handler)
    print ('weixin server is running at http://127.0.0.1:' + str(serverPort))
    #print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

