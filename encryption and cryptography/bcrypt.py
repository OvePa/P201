import bcrypt

password = b"password@educative"

salt_generation = bcrypt.gensalt(10)
print("Randomly generated salt after 10 rounds: ")
print(salt_generation)

password_hash = bcrypt.hashpw(password, salt_generation)
print("Password hashed after random generation of salt:")
print(password_hash)

password_match = bcrypt.checkpw(password, password_hash)
print("if the password matches with already hashed password:")
print(password_match)


"""
In the code above, after importing the bcrypt, salt will be generated by giving 
10 rounds (line 5). We can hash the password by passing arguments of the 
password provided and the salt created respectively (line 9). Then to check 
if the password hashed matches with already hashed passwords we will pass the 
provided password and the hashed password respectively (line 13).
"""