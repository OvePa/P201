"""
map
The map built-in also takes a function and an iterable and returns an iterator
that applies the function to each item in the iterable.
"""


def doubler(x):
    return x * 2


my_list = [1, 2, 3, 4, 5]
for item in map(doubler, my_list):
    print(item)


"""
How map() and filter() duplicates?

The map and filter functions basically duplicate the features of generator 
expressions in Python 3. 
"""


def doubler(x):
    return x * 2


my_list = [1, 2, 3, 4, 5]
print(list(map(doubler, my_list)))


# But we can do the same thing with a list comprehension:
def doubler(x):
    return x * 2


my_list = [1, 2, 3, 4, 5]
print([doubler(x) for x in my_list])


"""
What is the main difference between map and filter?

Answer
Map will be applied to all objects of iterable and filter will be applied to 
only those objects which hold true for the condition.
"""
