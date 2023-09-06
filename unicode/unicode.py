"""
One of the major changes in Python 3 was the move to make all strings Unicode.
Previously, there was a str type and a unicode type. For example:
"""
# Python 2
x = "blah"
print(type(x))

# y = u"blah" al ejecutar se elimina la u
y = "blah"
print(type(y))


# python 2 error, python 3 funciona
здравствуйте = "hello"
print(здравствуйте)

# Python 3
print(("abcdef" + chr(255)).encode("utf-8"))

print("it will print character: ")
print(b"\xa0".decode("ascii", "replace"))
## '�'
print("it will print space: ")
print(b"\xa0".decode("ascii", "ignore"))
## ''


u = chr(40960) + "abcd" + chr(1972)

print(u.encode("ascii", "ignore"))
# b'abcd'

print(u.encode("ascii", "replace"))
# b'?abcd?'

"""
For this example, we took a string and added a non-ASCII character to the 
beginning and the end of the string. Then we tried to convert the string to a 
bytes representation of the Unicode string using the encode method. The first 
attempt did not work and gave us an error. The next one used the ignore flag, 
which basically removed the non-ASCII characters from the string entirely. 
The last example uses the replace flag which just puts question marks in place 
for the unknown Unicode characters.

If we need to work with encodings a lot, Python also has a module called codecs 
that we should check out.
"""
