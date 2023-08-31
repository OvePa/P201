"""
The infinite iterators
The itertools package comes with three iterators that can iterate infinitely.
What this means is that when we use them, you need to understand that we will
need to break out of these iterators eventually or we’ll have an infinite loop.
"""
from itertools import count
from itertools import islice
from itertools import cycle
from itertools import repeat

# Need to break it
for i in count(10):
    if i > 20:
        break
    else:
        print(i)

# Use islice
for i in islice(count(20), 5):
    print(i)


# Cycle
count = 0
for item in cycle("ZYX"):
    if count > 10:
        break
    else:
        print(item)
        count += 1

# We can also use Python’s next built-in to iterate over the iterators
# we create with itertools:
polys = ["triangle", "square", "pentagon", "rectangle"]
iterator = cycle(polys)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


"""
The repeat iterator will return an object over and over again forever unless 
you set its time argument. It is quite similar to cycle except that it doesn’t 
cycle over a set of values repeatedly.
"""
repeat(5, 5)
repeat(5, 5)

iterator = repeat(5, 5)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
