# pip3 install cryptography

"""
We will see that cryptography installs a few dependencies along with itself.
Assuming that they all are completed successfully, we can try encrypting some text.
Let’s give the Fernet module a try. The Fernet module implements an easy-to-use
authentication scheme that uses a symmetric encryption algorithm which
guarantees that any message we encrypt with it cannot be manipulated or read
without the key we define. The Fernet module also supports key rotation via
MultiFernet.

"""
from cryptography.fernet import Fernet

cipher_key = Fernet.generate_key()
print(cipher_key)


cipher = Fernet(cipher_key)
text = b"My super secret message"
encrypted_text = cipher.encrypt(text)
print(encrypted_text)


decrypted_text = cipher.decrypt(encrypted_text)
print(decrypted_text)


"""
First off we need to import Fernet (Line 1). Next we generate a key. 
We print out the key to see what it looks like (Lines 2-3). As you can see, 
it’s a random byte string. If you want, you can try running the generate_key 
method a few times. The result will always be different. Next we create our 
Fernet cipher instance using our key (Line #7).

Now we have a cipher we can use to encrypt and decrypt our message (Lines 8-13). 
The next step is to create a message worth encrypting and then encrypt it using 
the encrypt method. We went ahead and printed out the encrypted text so you can 
see that you can no longer read the text. To decrypt our super secret message, 
we just call decrypt on our cipher and pass it the encrypted text. The result is 
we get a plain text byte string of our message.
"""
