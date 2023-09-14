from cryptography.fernet import Fernet

# encrypting
create_key = Fernet.generate_key()

with open("created.key", "wb") as created:
    created.write(create_key)

with open("created.key", "rb") as created:
    create_key = created.read()
    print(create_key)

key = Fernet(create_key)

with open("students.csv", "rb") as given_file:
    given = given_file.read()

encrypted_file = key.encrypt(given)

with open("encrypted.csv", "wb") as encrypted:
    encrypted.write(encrypted_file)

# decrypting
with open("encrypted.csv", "rb") as encrypted:
    encrypted_file = encrypted.read()

decrypted_file = key.decrypt(encrypted_file)

with open("decrypted.csv", "wb") as decrypted:
    decrypted.write(decrypted_file)
