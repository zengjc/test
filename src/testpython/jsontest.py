'''
Created on 2015年12月15日

@author: zjc
'''
import json
import collections

obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print (type(repr(obj)))
print (encodedjson)
print (type(encodedjson))


data={'filter':{'is_to_all':False,'group_id':'1'},'text':{'content':'this is text to all'},'msgtype':'text'}
# data={"touser":"oZ04NuJXV_hDosEQtlawWh8YpauU","msgtype":"text","text":{"content":"Hello World"}}
data=['1','2']
encodedjson = json.dumps(data,indent=2,sort_keys=True)
print (data)
print (encodedjson)

d=collections.OrderedDict()
d['touser']='oZ04NuJXV_hDosEQtlawWh8YpauU'
d['msgtype']='text'
d['text']={"content":"Hello World"}
print (d)
print (json.dumps(d))