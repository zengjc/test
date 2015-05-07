# -*- coding: utf-8 -*-
import socket

if "__main__" == __name__:


    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('localhost',8008))
    sock.send('0'.encode())
    
    szBuf = sock.recv(1024).decode()
    #byt = 'recv:' + szBuf.decode('gbk')
    print(szBuf)
    
    sock.close()
    print('end of the connecct')