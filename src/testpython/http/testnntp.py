'''
Created on 2015年12月17日

@author: zjc
'''
import nntplib
data = {'filter': {'is_to_all': False, 'group_id': 1},'msgtype': 'text'}
data.update({'text': {'content': 'this is content'}})
nntplib.post(url='https://api.weixin.qq.com/cgi-bin/message/mass/sendall',data=data)

