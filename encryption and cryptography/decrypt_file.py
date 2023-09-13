from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


from Crypto.PublicKey import RSA

code = "nooneknows"
key = RSA.generate(2048)
# print("key: ", key)
encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
with open("my_private_rsa_key.pem", "wb") as f:
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

code = "nooneknows"

with open("encrypted_data.bin", "rb") as fobj:
    private_key = RSA.import_key(open("my_private_rsa_key.pem").read(), passphrase=code)

    enc_session_key, nonce, tag, ciphertext = [
        fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
    ]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

print(data)

"""
If you followed the previous example, this code should be pretty easy to parse. 
In this case, we are opening our encrypted file for reading in binary mode. 
Then we import our private key. Note that when we import the private key, 
we must give it our passcode. Otherwise, we will get an error. Next, we read in 
our file. You will note that we read in the private key first, then the next 
16 bytes for the nonce, which is followed by the next 16 bytes which is the tag, 
and finally the rest of the file, which is our data.

Then we need to decrypt our session key, recreate our AES key and decrypt the data.

You can use PyCryptodome to do much, much more. However, we need to move on and 
see what else we can use for our cryptographic needs in Python.
"""
