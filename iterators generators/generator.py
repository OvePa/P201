"""
A generator works by “saving” where it last left off (or yielding) and giving
the calling function a value. So instead of returning the execution to the
caller, it just gives temporary control back. To do this magic, a generator
function requires Python’s yield statement.
"""


def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number


doubler = doubler_generator()
print(next(doubler))


print(next(doubler))


print(next(doubler))


def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"


gen = silly_generator()
print(next(gen))

print(next(gen))


# Generator and loops
def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"


gen = silly_generator()
for item in gen:
    print(item)
print(next(gen))

print(next(gen))


print(type(doubler))
