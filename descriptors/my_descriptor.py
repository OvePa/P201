class MyDescriptor:
    """
    A simple demo descriptor
    """

    def __init__(self, initial_value=None, name="my_var"):
        self.var_name = name
        self.value = initial_value

    def __get__(self, obj, objtype):
        print("Getting", self.var_name)
        return self.value

    def __set__(self, obj, value):
        msg = "Setting {name} to {value}"
        print(msg.format(name=self.var_name, value=value))
        self.value = value


class MyClass:
    desc = MyDescriptor(initial_value="Mike", name="desc")
    normal = 10


if __name__ == "__main__":
    c = MyClass()
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)

"""
Here we create a class and define three magic methods:

__init__: our constructor which takes a value and the name of our variable 
__get__: prints out the current variable name and returns the value 
__set__: prints out the name of our variable and the value we just assigned and sets the value itself 

Then we create a class that creates an instance of our descriptor as a class 
attribute and also creates a normal class attribute (linea 18-20). Then we run 
a few “tests” by creating an instance of our normal class and accessing our 
class attributes.

As we can see, when we access c.desc, it prints out our “Getting” message and 
we print out what it returns, which is “Mike”. Next we print out the regular 
class attribute’s value. Finally we change the descriptor variable’s value, 
which causes our “Setting” message to be printed. We also double-check the 
current value to make sure that it was actually set, which is why we see that 
last “Getting” message.

Python uses descriptors underneath the covers to build properties, 
bound / unbound methods and class methods. If we look up the property class 
in Python’s documentation, we will see that it follows the descriptor protocol 
very closely:

property(fget=None, fset=None, fdel=None, doc=None)

It clearly shows that the property class has a getter, setter and a deleting method.
"""
