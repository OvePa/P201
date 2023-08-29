"""
In this code, we decorate the function called a_function with another_function.
We can check a_function's name and docstring by printing them out using the
function’s __name__ and __doc__ properties.
"""


def another_function(func):
    """
    A function that accepts another function
    """

    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(), eval(func()))
        return val

    return wrapper


@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)
