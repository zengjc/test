'''
Created on 2015年12月15日

@author: zjc
'''
import httplib2
from urllib.parse import quote_plus    
import json
import collections

def getweixinaccesstoken():
    urlstr = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxdb883d2261ccd3e9&secret=2b1e52f89896d7f54dcde15a3b550539'
 
    h = httplib2.Http('.cache')
    response,content = h.request(urlstr)
 
    if 'access_token' in content.decode('utf-8'):
        access_token = eval(content.decode('utf-8'))['access_token']
        expires_in = int(eval(content.decode('utf-8'))['expires_in'])
    print ('有效期：' + str(expires_in) + '获取到的access_token为：' + access_token)
    return access_token
def getuserinfo():
    access_token='UZy2naKz-Fsq08MrzqZ75qvwoiGxvxAvn_5D6JBIncCHdzfp0P1crg-TlmM4095kPQaQ8uFfFiwIEiI0CHy5S2wRqUi71Q3uDQkQu3D0ig0TZXjAAAOUS'
    urlstr='https://api.weixin.qq.com/cgi-bin/groups/get?access_token=' + access_token
    h = httplib2.Http('.cache') 
    response,content = h.request(urlstr)

    #for item in response.items(): print(item)
    print(content.decode('utf-8'))
    
def sendtexttoall():
    import httplib2
    from urllib.parse import urlencode    
  
  #httplib2.debuglevel = 1

#   word='美国'
    access_token='gc_-LfE4349E3KZ_fbs8QFWksZ2iyjh7aYrNr2mYYdKMTexIMppM5pRxIfONtQf2yh0-_pEzg4iWEApcz_4GhUzLNjMyh-QBVJdo9My44S8APUjAHAIXC'
    urlstr = 'https://api.weixin.qq.com/cgi-bin/message/mass/sendall?access_token=' + access_token

#   data={'wordKey':word} 
  
    data={'filter':{'is_to_all':False,'group_id':'1'},'text':{'content':'this is text to all'},'msgtype':'text'}

    d=collections.OrderedDict()
    d['touser']='oZ04NuJXV_hDosEQtlawWh8YpauU'
    d['msgtype']='text'
#     d['text']={"content":"Hello World"}
#     datajson=json.dumps(data)
#     data={'filter':{'is_to_all':False,'group_id':'1'},'image':{'media_id':'123dsdajkasd231jhksad'},'msgtype':'image'}
    
#     data=b'{ "filter":{ "is_to_all":false "group_id":"1" }, "text":{ "content":"CONTENT2" }, "msgtype":"text"}'
     
    h = httplib2.Http('.cache')
    response,content = h.request(urlstr, 'POST', quote_plus(json.dumps(d)), headers={'Content-Type': 'application/x-www-form-urlencoded'})  

  #for item in response.items(): print(item)
    print(content.decode('utf-8'))

    print (json.dumps(d))


if __name__ == '__main__':
#     print (getweixinaccesstoken())
    getuserinfo()
#     sendtexttoall()
#     TestHttpPostx()
   