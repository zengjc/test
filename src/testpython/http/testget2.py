'''
Created on 2015年11月2日

@author: zjc
'''
#!/usr/bin/env python
# Submit GET Data - Chapter 6 - submit_get.py
import sys, urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error

def addGETdata(url, data):
    """Adds data to url.  Data should be a list or tuple consisting of 2-item
    lists or tuples of the form: (key, value).
    Items that have no key should have key set to None.
    A given key may occur more than once.
    """
    return url + '?' + urllib.parse.urlencode(data)

zipcode = 'get8080'
# url = addGETdata('http://www.wunderground.com/cgi-bin/findweather/getForecast',[('query', zipcode)])
url = addGETdata('http://127.0.0.1',[('query', zipcode)])

print("Using URL", url)
req = urllib.request.Request(url)
fd = urllib.request.urlopen(req)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data.decode('utf-8'))