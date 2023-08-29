"""
We can use it to create a new function with partial application of the arguments
and keywords that we pass to it. We can use partial to “freeze” a portion of our
function’s arguments and/or keywords which results in a new object. Another way
to put it is that partial creates a new function with some defaults.
"""
from functools import partial


from functools import partial


def add(x, y):
    """"""
    return x + y


def multiply(x, y):
    """"""
    return x * y


def run(func):
    """"""
    print(func())


def main():
    """"""
    a1 = partial(add, 1, 2)
    m1 = partial(multiply, 5, 8)
    run(a1)
    run(m1)


if __name__ == "__main__":
    main()

    # example
    p_add = partial(add, 2)
    print(p_add(4))
