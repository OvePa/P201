"""
Key Derivation

Python has pretty limited support for key derivation built into the standard
library. In fact, the only method that hashlib provides is the pbkdf2_hmac method,
which is the PKCS#5 password-based key derivation function. It uses HMAC as its
pseudorandom function. We might use something like this for hashing our password
as it supports salt and iterations. For example, if we have to use SHA-256,
we would need a salt of at least 16 bytes and a minimum of 100,000 iterations.

As a quick aside, a salt is just random data that we use as additional input
into our hash to make it harder to “unhash” our password.

salt is basically a configuration management tool that protects our password
from dictionary attacks and precomputed rainbow tables.
"""
import hashlib
import binascii

dk = hashlib.pbkdf2_hmac(
    hash_name="sha256",
    password=b"password@educative",
    salt=b"educative_salt",
    iterations=100000,
)
print(binascii.hexlify(dk))

"""
Here we create a SHA256 hash on a password using a lousy salt but with 100,000 
iterations (Lines 3-6). Of course, SHA is not actually recommended for creating 
keys or passwords. Instead, we should use something like scrypt instead.
"""
