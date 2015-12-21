'''
Created on 2015年11月2日

@author: zjc
'''
#!/usr/bin/env python
# Submit POST Data - Chapter 6 - submit_post.py
import sys, urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error

zipcode = 'I give you a post!'
url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast'
# url = 'http://127.0.0.1'
data = urllib.parse.urlencode([('query', zipcode)])
req = urllib.request.Request(url)
fd = urllib.request.urlopen(req, data.encode(encoding='utf_8', errors='strict'))
print (url + data)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data.decode('utf-8'))