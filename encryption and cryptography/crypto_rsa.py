"""
Creating an RSA key
If we want to encrypt our data with RSA, then we’ll need to either have access
to a public / private RSA key pair or we will need to generate our own. For this
example, we will just generate our own. Since it’s fairly easy to do, we will do
it in Python’s interpreter:
"""
from Crypto.PublicKey import RSA

code = "nooneknows"
key = RSA.generate(2048)
print("key: ", key)
encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
with open("my_private_rsa_key.bin", "wb") as f:
    f.write(encrypted_key)
with open("my_rsa_public.pem", "wb") as f:
    f.write(key.publickey().exportKey())

"""
First we import RSA from Crypto.PublicKey. Then we create a silly passcode. 
Next we generate an RSA key of 2048 bits. Now we get to the good stuff. 
To generate a private key, we need to call our RSA key instance’s exportKey 
method and give it our passcode, which PKCS standard to use and which encryption 
scheme to use to protect our private key. Then we write the file out to disk.

Next we create our public key via our RSA key instance’s publickey method. 
We used a shortcut in this piece of code by just chaining the call to exportKey 
with the publickey method call to write it to disk as well.
"""
