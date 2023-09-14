def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num

    return incrementer


c = counter()

print(c)


print(c())


print(c())


print(c())

"""
Now our incrementing function works as we expected it to. As a side note, 
this type of function is known as a closure. A closure is basically a block of 
code that “closes” nonlocal variables. The idea behind a closure is that we can 
reference variables that are defined outside of our function.

Basically nonlocal will allow us to assign to variables in an outer scope, 
but not in a global scope (line 4). So we can’t use nonlocal in our counter 
function because then it would try to assign to a global scope. Give it a try 
and we will quickly get a SyntaxError. Instead we must use nonlocal in a nested 
function.
"""
