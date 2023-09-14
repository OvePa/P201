from weakref import WeakKeyDictionary


class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()

    def __get__(self, instance_obj, objtype):
        return self.age.get(instance_obj, self.req_age)

    def __set__(self, instance, new_age):
        if new_age < 21:
            msg = "{name} is too young to legally imbibe"
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = new_age
        print("{name} can legally drink in the USA".format(name=instance.name))

    def __delete__(self, instance):
        del self.age[instance]


class Person:
    drinker_age = Drinker()

    def __init__(self, name, age):
        self.name = name
        self.drinker_age = age


p = Person("Miguel", 30)
p = Person("Niki", 13)

"""
Once again, we create a descriptor class. In this case, we use Python’s weakref 
library’s WeakKeyDictionary, which is a neat class that creates a dictionary 
that maps keys weakly. What this means is that when there are no strong references 
to a key in the dictionary, that key and its value will be discarded. We are 
using that in this example to prevent our Person instances from hanging around 
indefinitely.

Anyway, the part of the descriptor that we care most about is in our __set__ method. 
Here we check to see that the instance’s age parameter is greater than 21, 
which is what we would need to be in the USA if we wanted to drink an alcoholic 
beverage. If our age is lower, then it will raise an exception. Otherwise it will 
print out the name of the person and a message. To test out our descriptor, 
we create two instances with one that is greater than 21 in age and one that is less.

That obviously worked the way it was supposed to, but it’s not really obvious 
how it worked. The reason this works the way it does is that when we go to 
set drinker_age, Python notices that it is a descriptor. Python knows that 
drinker_age is a descriptor because we defined it as such when we created it as 
a class attribute:

drinker_age = Drinker()

So when we go to set it, we actually call our descriptor’s __set__ method which 
passes in the instance and the age that we are trying to set. If the age is less 
than 21, then we raise an exception with a custom message. Otherwise we print out 
a message that we are old enough.

Getting back to how this all works, if we try to print out the drinker_age, 
Python would execute Person.drinker_age.__get__. Since drinker_age is a descriptor, 
its __get__ is what actually gets called. If we wanted to set the drinker_age, 
we would do this:

p.drinker_age = 32

Python would then call Person.drinker_age.__set__ and since that method is also 
implemented in our descriptor, then the descriptor method is the one that gets called. 
Once we trace our way through the code execution a few times, we will quickly 
see how this all works.

The main thing to remember is that descriptors are linked to classes and not to 
instances.
"""
