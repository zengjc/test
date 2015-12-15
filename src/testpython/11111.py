# import simplejson
str = None

def test1():
    namelist = '[sdfsdfsdf][sfsdfsd][r54r5]'
    if '[' + 'sfsdfsd' + ']' in namelist:
        print ('有name')
        
    info = "{'name' : 'jay', 'sex' : 'male', 'age': 22}"
    jsoninfo = eval(info)
    print (jsoninfo) 
    print (type(jsoninfo))
def test2():
    if str == None:
        print ('str is none')
    else:
        print ('str is not none')
        
    
    str1 = ''
    if str1 == '':
        print ('str1 is none')
    else:
        print ('str1 is not none')

def test3():
    int1 = 1
    int2 = 1
    if int1==0 and int2==0 :
        print ('都是0')
    else :
        print ('有1')
        
    if not (int1 and int2) :
        print ('都是0')
    else :
        print ('有1')
        
        
if __name__ == '__main__':
    test3()