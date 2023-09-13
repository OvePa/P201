from Crypto.Protocol.KDF import scrypt

password = b"password@educative"
salt = b"educative_salt"
key = scrypt(password, salt, 16, N=2**14, r=8, p=1)
print(key)

"""
In the above code, after importing the scrypt. We will provide the password 
and salt (lines 3-4). For key generation, multiple arguments will be passed; 
password, salt, number of iterations, numbers of bytes to be generated as output, 
block size, and parallelism factor respectively (line 5).


"""
