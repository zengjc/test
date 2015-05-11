# -*- coding: UTF-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import hashlib
import cgi

import io,shutil  
import urllib
import os, sys

from testpython.weixin import funcIf4weixin
import imp

def update_function_module(mode='remote'):
    if mode == 'remote':
        import os
        os.system('git pull')
    imp.reload(funcIf4weixin)

class Handler( BaseHTTPRequestHandler ):
    TOKEN = 'zengjingchao17'   #make it invisible later

    def do_GET(self):
        print (threading.currentThread().getName())
        print (self.path)
        text = 'Constructing...\n'
        if self.verifyWeixinHeader():
            if self.path.startswith('/update?'):
                update_function_module()
                text = 'updated'
            elif self.path.startswith('/updatelocal?'):
                update_function_module('local')
                text = 'updated'                
            else:
                text = self.receivedParams['echostr']
        self.sendResponse(str(text).encode())
        return

    def do_POST(self):
        if not self.verifyWeixinHeader():
            return
#         form = cgi.FieldStorage(
#              fp=self.rfile,
#              headers=self.headers,
#              
#              environ={'REQUEST_METHOD':'POST',
#                       'CONTENT_TYPE':'text/xml', #硬编码
#                       })
# #              environ={'REQUEST_METHOD':'POST',
# #                       'CONTENT_TYPE':self.headers['Content-Type'],
# #                       })
#         if form.file:      
#             data = form.file.read()   
#             print (data)      
#         else:                          
#             print ("data is None")
        mpath,margs=urllib.parse.splitquery(self.path)
        data = self.rfile.read(int(self.headers['content-length']))
        print ('data = ' + str(data))
        #data='<xml><ToUserName><![CDATA[{TO_USER}]]></ToUserName>\n<FromUserName><![CDATA[{FROM_USER}]]></FromUserName>\n<CreateTime>{TIME_STEMP}</CreateTime>\n<MsgType><![CDATA[text]]></MsgType>\n<Content><![CDATA[{RESPONSE_CONTENT}]]></Content>\n<MsgId>6146033119142104914</MsgId>\n</xml>'
        self.send_response(200)
        self.end_headers()
        
        #self.do_action(mpath, datas)

        worker = funcIf4weixin.msgHandler(data)
        self.wfile.write(worker.response().encode('UTF-8'))


    
    def verifyWeixinHeader(self):
        self.receivedParams = self.requestGet()
        print (self.receivedParams)
        return (self.receivedParams and self.isWeixinSignature())

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


    def isWeixinSignature(self):
        signature = self.receivedParams['signature']
        timestamp = self.receivedParams['timestamp']
        nonce = self.receivedParams['nonce']
        #都需要加上encode
        wishSignature = self.localSignature(self.TOKEN.encode(encoding='utf_8'), timestamp.encode(encoding='utf_8'), nonce.encode(encoding='utf_8'))
        print (signature, wishSignature)
        return signature == wishSignature
        

        
        
    def sendResponse(self, text):
        self.send_head(str(text).encode())
        self.wfile.write(text)
        self.wfile.close()
    
    
    def send_head(self, text):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        fullLength = len(text)
        print (fullLength, text)
        self.send_header("Content-Length", str(fullLength))
        self.end_headers()
        return

        
    def localSignature(self, token, timestamp, nonce):
        items = [token, timestamp, nonce]
        items.sort()
        sha1 = hashlib.sha1()
        list(map(sha1.update,items))#
        hashcode = sha1.hexdigest()
        return hashcode

    

        
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    
if __name__ == '__main__':
    serverPort = 80
    server_address = ('', serverPort) 
    try:
        #f = open('TOKENFILE')
        #token = f.read().strip()
        token = 'zengjingchao_office_stg'
        Handler.TOKEN = token
    except Exception as inst:
        print (inst)
        
    server = ThreadedHTTPServer( server_address, Handler)
    print ('Download server is running at http://127.0.0.1:' + str(serverPort))
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
