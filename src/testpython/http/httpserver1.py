from http.server import HTTPServer,BaseHTTPRequestHandler  
import io,shutil  
  
port=80

class MyHttpHandler(BaseHTTPRequestHandler):  
    def do_GET(self):  
#         i=0
#         i+=1
        r_str="Hello Alan!这是访问计数器：" #+ str(i)  
        enc="UTF-8"  
        encoded = ''.join(r_str).encode(enc)  
        f = io.BytesIO()  
        f.write(encoded)  
        f.seek(0)  
        self.send_response(200)  
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))  
        self.end_headers()  
        shutil.copyfileobj(f,self.wfile)  
  
httpd=HTTPServer(('',port),MyHttpHandler)  
print("Server started on 127.0.0.1,port " + str(port))  
httpd.serve_forever() 