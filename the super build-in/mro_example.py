class X:
    def __init__(self):
        print("X")
        super().__init__()


class Y:
    def __init__(self):
        print("Y")
        super().__init__()


class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)


"""
Here we create three classes. The first two just print out the name of the class 
and the last one inherits from the previous two.

As we can see, when we instantiate the classes, each of the parent classes prints 
out its name. Then we get the Method Resolution Order, which is ZXY and object.
"""
