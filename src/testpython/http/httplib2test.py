# -*- coding: UTF-8 -*-
'''
Created on 2015年5月6日

@author: zjc
'''
import httplib2

h = httplib2.Http('.cache2')

response, content = h.request('http://127.0.0.1:8081/?wordKey=alan2')

print (response.status)
print (content[:52])
print (len(content))