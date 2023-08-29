"""
What is contextlib?
Python 2.5 not only added the with statement, but it also added the contextlib
module. This allows us to create a context manager using contextlib’s
contextmanager function as a decorator.
"""
from contextlib import contextmanager


@contextmanager
def file_open(path):
    try:
        f_obj = open(path, "w")
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print("Closing file")
        f_obj.close()


if __name__ == "__main__":
    with file_open("test.txt") as fobj:
        fobj.write("Testing context managers")
