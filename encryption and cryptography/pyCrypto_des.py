from Crypto.Cipher import DES

key = b"abcdefgh"


def pad(text):
    while len(text) % 8 != 0:
        text += b" "
    return text


des = DES.new(key, DES.MODE_ECB)
text = b"Python rocks!"
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
print(encrypted_text)

# descrypt
print(des.decrypt(encrypted_text))
"""
This code is a little confusing, so let’s spend some time breaking it down. 
First off, it should be noted that the key size for DES encryption is 8 bytes, 
which is why we set our key variable to a size letter string (Line 4). 
The string that we will be encrypting must be a multiple of 8 in length, so we 
create a function called pad that can pad any string out with spaces until 
it’s a multiple of 8. Next we create an instance of DES and some text that we 
want to encrypt. We also create a padded version of the text. Just for fun, 
we attempt to encrypt the original unpadded variant of the string which raises
a ValueError. Here we learn that we need that padded string after all, so we 
pass that one in instead. As you can see, we now have an encrypted string!
"""

"""
Fortunately, that is very easy to accomplish as all we need to do is call the 
decrypt method on our des object to get our decrypted byte string back. Our next 
task is to learn how to encrypt and decrypt a file with PyCrypto using RSA. 
But first we need to create some RSA keys!


"""
