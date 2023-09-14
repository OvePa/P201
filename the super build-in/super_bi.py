class MyParentClass:
    def __init__(self):
        pass


class SubClass(MyParentClass):
    def __init__(self):
        super().__init__()


"""
The first change we will notice is that the parent class no longer needs to be 
explicitly based on the object base class. The second change is the call to super. 
We no longer need to pass it anything and yet super does the right thing implicitly. 
Most classes actually have arguments passed to them though, so let’s look at 
how the super signature changes in that case:
"""


class MyParentClass2:
    def __init__(self, x, y):
        pass


class SubClass2(MyParentClass2):
    def __init__(self, x, y):
        super().__init__(x, y)


"""
Here we just need to call the super's _init_ method and pass the arguments along. 
It’s still nice and straightforward.
"""
