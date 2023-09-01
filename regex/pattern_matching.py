"""
Escape codes |       Use
-----------------------------------------
    d        |  Matches digit
    D        |  Matches non-digit
    s        |  Matches whitespace
    S        |  Matches non-whitespace
    w        |  Matches alphanumeric
    W        |  Matches non-alphanumeric
"""


"""
Special Note: When we compile patterns, they will get automatically cached so 
if we aren’t using a lot of regular expressions in our code, then we may not 
need to save the compiled object to a variable.
"""
import re

text = "The ants go marching one by one"

strings = ["the", "one by"]

for string in strings:
    regex = re.compile(string)
    print("regex-> ", regex)
    match = re.search(string, text)
    print("match", match)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print("->", text[match.start() : match.end()])
    else:
        print('Did not find "{}"'.format(string))


# findall()
print("Findall()")
silly_string = "the cat in the hat"
pattern = "the"
print(re.findall(pattern, silly_string))


# finditer()
print("Finditer()")


silly_string = "the cat in the hat"
pattern = "the"

for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(), end=match.end()
    )
    print(s)


# Backslashes
testing_string = 'python ""'
print(testing_string)  # python ""

testing_string = 'python "\\"'
print(testing_string)  # python "\"

testing_string = r'python "\"'
print(testing_string)  # python "\"
