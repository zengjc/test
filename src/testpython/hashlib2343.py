import hashlib  
m = hashlib.md5()
str="Nobody inspects the spammish repetition"
m.update(str.encode(encoding='utf_8')) #参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误  
md5value=m.hexdigest()  
print(md5value)  #bb649c83dd1ea5c9d9dec9a18df0ffe9

def localSignature( token, timestamp, nonce):
    items = [token, timestamp, nonce]
    items.sort()
    sha1 = hashlib.sha1()
    list(map(sha1.update,items))#
    hashcode = sha1.hexdigest()
    return hashcode

TOKEN='TOKENTOKEN'
signature = 'signature'
timestamp = 'timestamp'
nonce = 'timestamp'
wishSignature = localSignature(TOKEN.encode(encoding='utf_8'), timestamp.encode(encoding='utf_8'), nonce.encode(encoding='utf_8'))

print (wishSignature)