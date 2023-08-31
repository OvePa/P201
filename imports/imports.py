# regular imports
import sys, os, time  # it goes against the Python Style Guide’s recommendations

# of putting each import on its own line.

import urllib.error  # We won’t see these very often, but they’re good to know about.

# "from module import something"
from functools import lru_cache
from os import *

# from os import (path, walk, unlink, uname,
#                 remove, rename )
# from os import path, walk, unlink, uname, \
#            remove, rename


# relative imports
"""
PEP 328 describes how relative imports came about and what specific syntax was 
chosen. The idea behind it was to use periods to determine how to relatively 
import other packages / modules. The reason was to prevent the accidental 
shadowing of standard library modules.

my_package/
    __init__.py
    subpackage1/
        __init__.py
        module_x.py
        module_y.py
    subpackage2/
        __init__.py
        module_z.py
    module_a.py
"""
# In the top-level _init_.py, put the following code in place:
from . import subpackage1
from . import subpackage2

# Next navigate down in subpackage1 and edit its _init_.pyto have the following contents:
from . import module_x
from . import module_y

# Now edit module_x.py such that it has the following code:
from .module_y import spam as ham


def main():
    ham()


# Finally edit module_y.py to match this:
def spam():
    print("spam " * 3)


# Optional imports#
"""
Optional imports are used when we have a preferred module or package that we 
want to use, but we also want a fallback in case it doesn’t exist.
"""
try:
    # For Python 3
    from http.client import responses
except ImportError:  # For Python 2.5-2.7
    try:
        from httplib import responses  # NOQA
    except ImportError:  # For Python 2.4
        from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH
    responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])


try:
    from urlparse import urljoin
    from urllib2 import urlopen
except ImportError:
    # Python 3
    from urllib.parse import urljoin
    from urllib.request import urlopen

# Local imports
"""
When we import our module into local scope it is called local import. 
When we do our imports at the top of our Python script file, that is importing 
the module into global scope, which means that any functions or methods that 
follow will be able to use it.
"""

import sys  # global scope


def square_root(a):
    # This import is into the square_root functions local scope
    import math

    return math.sqrt(a)


def my_pow(base_num, power):
    return math.pow(base_num, power)


# Common import pitfalls
"""
Circular imports
Circular imports happen when we create two modules that import each other. 
Let’s look at an example as that will make it quite clear what we are referring to.
"""
# a.py
import b


def a_test():
    print("in a_test")
    b.b_test()


a_test()

# b.py
import a


def b_test():
    print('In test_b"')
    a.a_test()


b_test()

# Shadowed imports
"""
Shadow imports (AKA name masking) happen when the programmer creates a module 
with the same name as a Python module
"""
# https://peps.python.org/pep-0302/
if __name__ == "__main__":
    # This won't work!
    main()
    """
    Traceback (most recent call last):
      File "main.py", line 1, in <module>
        from . module_y import spam as ham
    SystemError: Parent module '' not loaded, cannot perform relative import
    """
    # local import
    print(square_root(49))
    print(my_pow(2, 3))  # error
    """
    Traceback (most recent call last):
    File "main.py", line 13, in <module>
    print(my_pow(2, 3))
    File "main.py", line 9, in my_pow
    return math.pow(base_num, power)
    NameError: name 'math' is not defined
    """
