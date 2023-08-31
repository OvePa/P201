"""
To make things extra clear, let’s go over a couple of definitions:

iterable - an object that has the _iter_ method defined.
iterator - an object that has both _iter_ and _next_ defined where _iter_ will
return the iterator object and _next_ will return the next element in the iteration.
"""
# Lists are iterable but not an iterator.

my_list = [1, 2, 3]
next(my_list)
# we can make a list an iterator

print(iter(my_list))


list_iterator = iter(my_list)
print(next(list_iterator))


print(next(list_iterator))


print(next(list_iterator))


print(next(list_iterator))

"""
When we use a loop to iterate over the iterator, we don’t need to call next and 
we also don’t have to worry about the StopIteration exception being raised.
"""
my_list = [1, 2, 3]
for item in iter(my_list):
    print(item)
