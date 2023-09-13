from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from Crypto.PublicKey import RSA

code = "nooneknows"
key = RSA.generate(2048)

encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
with open("my_private_rsa_key.bin", "wb") as f:
    f.write(encrypted_key)
with open("my_rsa_public.pem", "wb") as f:
    f.write(key.publickey().exportKey())

with open("encrypted_data.bin", "wb") as out_file:
    recipient_key = RSA.import_key(open("my_rsa_public.pem").read())
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    data = b"blah blah blah Python blah blah"
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(ciphertext)
    print("data is:")
    print(data)
    print("tag is:")
    print(tag)
    print("ciphertext is:")
    print(ciphertext)


"""
The first three lines cover our imports from PyCryptodome. Next we open up a 
file to write to. Then we import our public key into a variable and create a 
16-byte session key. For this example we are going to be using a hybrid 
encryption method, so we use PKCS\#1 OAEP, which is Optimal asymmetric encryption 
padding. This allows us to write a data of an arbitrary length to the file. 
Then we create our AES cipher, create some data and encrypt the data. This will 
return the encrypted text and the MAC. Finally we write out the nonce, MAC (or tag) 
and the encrypted text.
"""

"""
As an aside, a nonce is an arbitrary number that is only used for cryptographic 
communication. They are usually random or pseudorandom numbers. For AES, it must 
be at least 16 bytes in length. Feel free to try opening the encrypted file in 
your favorite text editor. You should just see gibberish.
"""
