import httplib2
httplib2.debuglevel = 1
h = httplib2.Http('.cache')
response, content = h.request('http://tieba.baidu.com/p/3620088728#')
len(content)
response.status
response.fromcache


