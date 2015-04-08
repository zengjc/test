# -*- coding: UTF-8 -*-  
import os
import humansize

print(os.getcwd())
print(os.path.realpath('feed.xml'))

#os.chdir('E\:\python')
a_list=[1,2,3,4,5]
a_list2=[num *2 for num in a_list]
a_list2
username='usern'
password = 'pass'
"{0}'s password is {1}".format(username, password)
si=humansize.SUFFIXES[1000]
print(si)
print('1000{0[0]} = 1{0[1]}'.format(si))
print('1000' + si[0] + ' = 1' + si[1])

s = '''Finished files are the re
 sult of years of scientif
 ic study combined with the
 experience of years'''
print(s.splitlines())
print(s.lower())
print(s.count('f'))
print(s.count('F'))
query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list=query.split('&')
print(a_list)
listoflist=[v.split('=',1) for v in a_list]
print(listoflist)
a_dict=dict(listoflist)
print(a_dict)
a_string = 'My alphabet starts where your alphabet ends.'
print(a_string[2:4])
by=b'abcde\x65'
by_b=b'\xe5\x9b\x9e\xe5\xa4\x8d\xef\xbc\x9a\xe3\x80\x90\xe4\xba\xa4\xe6\x98\x93\xe8\xbd\xac\xe8\xae\xa9\xe4\xb8\x93\xe7\x94\xa8\xe8\xb4\xb4\xe3\x80\x912014_\xe4\xb8\x8a\xe6\xb5\xb7\xe9\xaa\x91\xe8\xa1\x8c\xe5\x90\xa7_\xe7\x99\xbe\xe5\xba\xa6\xe8\xb4\xb4\xe5\x90\xa7'
print(by)
a_string = '深入 Python'
by = a_string.encode('utf‐8')
print(by)
by = a_string.encode('big5')
print(by)
roundtrip = by.decode('big5')
print(type(by))
by = a_string.encode('utf‐8')
roundtrip = by.decode('utf‐8')
print('roundtrip:'+roundtrip)
print('测试转码:'+'中国上海'.encode('utf_8').decode('utf_8'))
print('测试转码:'+by_b.decode('utf_8'))
print('abcde'.replace('d', '1'))

