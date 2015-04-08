import urllib.request
a_url = 'http://tieba.baidu.com/p/2796411864?pn=8'
data = urllib.request.urlopen(a_url).read()
type(data)
print(data)


from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
from urllib.request import urlopen
response = urlopen('http://tieba.baidu.com/p/3620088728#')
print(response.headers.as_string())
data = response.read()
print(len(data))