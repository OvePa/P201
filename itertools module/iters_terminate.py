"""
Following are the finite iterators of itertools:

accumulate(iterable)
chain(*iterables)
chain.from_iterable(iterable)
compress(data, selectors)
dropwhile(predicate, iterable)
filterfalse(predicate, iterable)
groupby(iterable, key=None)
islice(iterable, start, stop)
starmap(function, iterable)
takewhile(predicate, iterable)
tee(iterable, n=2)
zip_longest(*iterables, fillvalue=None)

"""
from itertools import accumulate
import operator

"""
accumulate(iterable)

The accumulate iterator will return accumulated sums or the accumulated results 
of a two argument function that we can pass to accumulate. The default of 
accumulate is addition
"""
print(list(accumulate(range(10))))
print(list(accumulate(range(1, 5), operator.mul)))


"""
chain(*iterables)

The chain iterator will take a series of iterables and basically flatten them 
down into one long iterable. Basically we had a list with some items already 
in it and two other lists that we wanted to add to the original list, but we 
only wanted to append the items in each list to the original list instead of 
creating a list of lists. 
"""
from itertools import chain

my_list = ["foo", "bar"]
numbers = list(range(5))
cmd = ["ls", "/some/dir"]
my_list = list(chain(["foo", "bar"], cmd, numbers))

print(my_list)
# ['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]


# Without itertools
my_list = ["foo", "bar"]
numbers = list(range(5))
cmd = ["ls", "/some/dir"]
my_list += cmd + numbers
print(my_list)
# ['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]

"""
chain.from_iterable(iterable)

We can also use a method of chain called from_iterable. This method works 
slightly differently than using chain directly. Instead of passing in a series 
of iterables, we have to pass in a nested list:
"""
numbers = list(range(5))
cmd = ["ls", "/some/dir"]

print(list(chain.from_iterable([cmd, numbers])))
# ['ls', '/some/dir', 0, 1, 2, 3, 4]


"""
compress(data, selectors)

he compress sub-module is useful for picking the first iterable values according 
to the second iterable Boolean values. This works by making the second iterable 
a list of Booleans (or ones and zeroes which amounts to the same thing).
"""
from itertools import compress

letters = "ABCDEFG"
bools = [True, False, True, True, False]
print(list(compress(letters, bools)))
# ['A', 'C', 'D']


"""
dropwhile(predicate, iterable)

There is a neat little iterator contained in itertools called dropwhile. 
This fun iterator will drop elements as long as the filter criteria is True. 
Because of this, we will not see any output from this iterator until the 
predicate becomes False. This can make the start-up time lengthy, so it’s 
something to be aware of.
"""
from itertools import dropwhile

print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))
# [6, 4, 1]


def greater_than_five(x):
    return x > 5


print(list(dropwhile(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
# [1, 2, 3, 10]


"""
filterfalse(predicate, iterable)

The filterfalse function from itertools is very similar to dropwhile. However 
instead of dropping values that match True, filterfalse will only return those 
values that evaluated to False.
"""
from itertools import filterfalse


def greater_than_five(x):
    return x > 5


print(list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
# [1, 2, 3]

"""
groupby(iterable, key=None)

The groupby iterator will return consecutive keys and groups from your iterable. 
This one is kind of hard to wrap our heads around without seeing an example.
"""
from itertools import groupby

vehicles = [
    ("Ford", "Taurus"),
    ("Dodge", "Durango"),
    ("Chevrolet", "Cobalt"),
    ("Ford", "F150"),
    ("Dodge", "Charger"),
    ("Ford", "GT"),
]

sorted_vehicles = sorted(vehicles)

for key, group in groupby(sorted_vehicles, lambda make: make[0]):
    for make, model in group:
        print("{model} is made by {make}".format(model=model, make=make))
    print("**** END OF GROUP ***\n")
"""
Here we import groupby and then create a list of tuples. Then we sort the data 
so it makes more sense when we output it and it also let’s groupby actually 
group items correctly. Next we actually loop over the iterator returned by 
groupby which gives us the key and the group. Then we loop over the group and 
print out what’s in it."""


"""
islice(iterable, start, stop)

islice is an iterator that returns selected elements from the iterable. 
That’s kind of an opaque statement. Basically what islice does is take a slice 
by index of our iterable (the thing we iterate over) and returns the selected 
items as an iterator. There are actually two implementations of islice. 
There’s itertools.islice(iterable, stop) and then there’s the version of islice 
that more closely matches regular Python slicing: 
islice(iterable, start, stop[, step]).
"""
from itertools import islice

iterator = islice("123456", 4)
print(next(iterator))  #'1'

print(next(iterator))  #'2'

print(next(iterator))  #'3'

print(next(iterator))  #'4'

# print (next(iterator))
# Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 15, in <module>
# print (next(iterator))
# StopIteration:

from itertools import islice
from itertools import count

print("*" * 6)
for i in islice(count(), 3, 15):
    print(i)


"""
starmap(function, iterable)
The starmap tool will create an iterator that can compute using the function 
and iterable provided. As the documentation mentions, “the difference between 
map() and starmap() parallels the distinction between function(a,b) 
and function(*c).
”"""
from itertools import starmap


def add(a, b):
    return a + b


print("*" * 6)
for item in starmap(add, [(2, 3), (4, 5)]):
    print(item)


"""
takewhile(predicate, iterable)

The takewhile module is basically the opposite of the dropwhile iterator that 
we looked at earlier. takewhile will create an iterator that returns elements 
from the iterable only as long as our predicate or filter is True. 
"""
from itertools import takewhile

print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))
# [1, 4]


"""
tee(iterable, n=2)

tee defaults to 2.
The tee tool will create n iterators from a single iterable. What this means 
is that we can create multiple iterators from one iterable. 
"""
from itertools import tee

data = "ABCDE"
iter1, iter2 = tee(data)
for item in iter1:
    print(item)


for item in iter2:
    print(item)


"""
zip_longest(*iterables, fillvalue=None)

The zip_longest iterator can be used to zip two iterables together. If the 
iterables don’t happen to be the same length, then we can also pass in a 
fillvalue. 
"""
from itertools import zip_longest

for item in zip_longest("ABCD", "xy", fillvalue="BLANK"):
    print(item)

# ('A', 'x')
# ('B', 'y')
# ('C', 'BLANK')
# ('D', 'BLANK')
"""It should be noted that if the iterable(s) passed to zip_longest have the 
potential to be infinite, then we should wrap the function with something like 
islice to limit the number of calls."""
