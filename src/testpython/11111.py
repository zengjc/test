'''
Created on 2013-12-3


@author: Administrator
'''
from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200);
        self.send_header('Content-type','text/html');
        self.end_headers()
        
    def do_HEAD(self):
        self._writeheaders()
        
    def do_GET(self):
        self._writeheaders()
        self.wfile.write("""
        <html>
        <head>
        <title>basehttp</title>
        </head>
        <body>this is body</body>
        </html>
        """) 
        
serveraddr = ('', 7070)
sevr = HTTPServer(serveraddr, RequestHandler)    
sevr.serve_forever()   