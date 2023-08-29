"""
Python recently added partial support for function overloading in Python 3.4.
They did this by adding a neat little decorator to the functools module called
singledispatch. This decorator will transform our regular function into a single
dispatch generic function. Note however that singledispatch only happens based
on the first argument’s type.
"""
from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported type")


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == "__main__":
    add(1, 2)
    add("Python", "Programming")
    add([1, 2, 3], [5, 6, 7])

    print(add.registry.keys())
    # add({"a": 1}, {"b": 2})  # error, unsupported type
