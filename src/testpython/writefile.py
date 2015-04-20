#create by zjc
fileo=open("E:\\python\\test4read.txt",encoding='GBK')
try:
    textdata=fileo.read()
finally:
    fileo.close()

fileout=open("E:\\python\\test4write.txt",'w')
fileout.write(textdata)
fileout.close()



