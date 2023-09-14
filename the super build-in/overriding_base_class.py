class Base:
    var = 5

    def __init__(self):
        pass


class X(Base):
    def __init__(self):
        print("X")
        super().__init__()


class Y(Base):
    var = 10

    def __init__(self):
        print("Y")
        super().__init__()


class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)
print(super(Z, z).var)

"""
So in this example, we create a Base class with a class variable set to a value of 10.
Then we create subclasses of our Base class: X and Y. Y overrides the Base class’s 
class variable and sets it to 10. Finally, we create class Z which inherits 
from X and Y. When we call super on class Z, which class variable will get printed?

Let’s parse this out a bit. Class Z inherits from X and Y. So when we ask it 
what its var is, the MRO will look at X to see if it is defined. It’s not there, 
so it moves on to Y. Y has it, so that is what gets returned. Try adding a class 
variable to X and we will see that it overrides Y because it is first in the 
Method Resolution Order.

There is a wonderful document that a fellow named Michele Simionato created that 
describes Python’s Method Resolution Order in detail. It’s a long read and we’ll 
probably need to re-read portions of it a few times, but it explains MRO very well. 
By the way, we might note that this article is labeled as being for Python 2.3, 
but it still applies even in Python 3, even though the calling of super is a bit 
different now.

The super method was updated slightly in Python 3. In Python 3, super can figure 
out what class it is invoked from as well as the first argument of the containing 
method. It will even work when the first argument is not called self! This is 
what we see when we call super() in Python 3. In Python 2, we would need to call 
super(ClassName, self), but that is simplified in Python 3.

Because of this fact, super knows how to interpret the MRO and it stores this 
information in the following magic properties: __thisclass__ and __self_class__.
"""
