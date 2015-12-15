# -*- coding: UTF-8 -*-
import httplib2
from urllib.parse import urlencode    

def TestHttpGet():

    #httplib2.debuglevel = 1

    word='中国'
    urlstr = 'http://127.0.0.1' + '?wordKey=' + word

    h = httplib2.Http('.cache') 
    response,content = h.request(urlstr)

    #for item in response.items(): print(item)
    print(content.decode('utf-8'))
    #print(content)

def TestHttpPost():

  #httplib2.debuglevel = 1

  word='美国'
  urlstr = 'http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString'

  data={'wordKey':word} 

  h = httplib2.Http('.cache')
  response,content = h.request(urlstr, 'POST', urlencode(data), headers={'Content-Type': 'application/x-www-form-urlencoded'})  

  #for item in response.items(): print(item)
  print(content.decode('utf-8'))
  #print(content)

def TestHttpPostx():

  #httplib2.debuglevel = 1

  word='美国'
  urlstr = 'http://cup.xkqh.com/jq/vote2/364'

  data={'wordKey':word} 

  h = httplib2.Http('.cache')
  response,content = h.request(urlstr, 'POST', urlencode(data), headers={'Content-Type': 'application/x-www-form-urlencoded'})  

  #for item in response.items(): print(item)
  print(content.decode('utf-8'))
  #print(content)

#TestHttpGet()
#TestHttpPost()
def TestHttpGet127():

    #httplib2.debuglevel = 1

    #word='中国'
#     urlstr = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxa0e98fcaf97f46b6&secret=f397e859666081663a157e612e8df691'
# 
#     h = httplib2.Http('.cache')
#     response,content = h.request(urlstr)
# 
#     #for item in response.items(): print(item)
#     print(content.decode('utf-8'))
#     print (type(content.decode('utf-8'))) 
#     if 'access_token' in content.decode('utf-8'):
#         access_token = eval(content.decode('utf-8'))['access_token']
#         expires_in = int(eval(content.decode('utf-8'))['expires_in'])
#     print ('获取到的access_token为：' + access_token)
#     print (type(access_token))
    access_token = 'Pa44q3L39s-yg17XJTbGAZY64JaSVRZvFqzTJOShFoNNl8Jif82ijKZLn34UD5M3VPl0rXSWfhwrLrOT8YCF-lcaWXexVW9JHOyBJowWj-0'
    usrstr2='https://api.weixin.qq.com/cgi-bin/user/get?access_token=' + access_token + '&next_openid=oZ04NuJXV_hDosEQtlawWh8YpauU'
    h = httplib2.Http('.cache')
    response,content = h.request(usrstr2)
    print('第二次请求返回值：' + content.decode('utf-8'))
    
def getweixinaccesstoken():
    urlstr = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxa0e98fcaf97f46b6&secret=f397e859666081663a157e612e8df691'
 
    h = httplib2.Http('.cache')
    response,content = h.request(urlstr)
 
    if 'access_token' in content.decode('utf-8'):
        access_token = eval(content.decode('utf-8'))['access_token']
        expires_in = int(eval(content.decode('utf-8'))['expires_in'])
    print ('有效期：' + str(expires_in) + '获取到的access_token为：' + access_token)
    return access_token

if __name__ == '__main__':
    print (TestHttpGet())
#     TestHttpPostx()
    
