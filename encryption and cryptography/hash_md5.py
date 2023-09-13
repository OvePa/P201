import hashlib

md5 = hashlib.md5()

md5.update(b"Python rocks!")
print(md5.digest())

"""
Let’s take a moment to break this down a bit. First off, we import hashlib and 
then we create an instance of an md5 HASH object. Next we add some text to the 
hash object and we get a traceback. It turns out that to use the md5 hash, we 
have to pass it a byte string instead of a regular string. So we try that and 
then call its digest method to get our hash.
"""
