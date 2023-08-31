"""
combinations(iterable, r)

If we have the need to create combinations, Python has we covered with itertools.
combinations. What combinations allows you to do is create an iterator from an
iterable that is some length long.
"""

from itertools import combinations

print(list(combinations("WXYZ", 2)))

for item in combinations("WXYZ", 3):
    print("".join(item))


"""
combinations_with_replacement(iterable, r)

The combinations_with_replacement iterator is very similar to combinations. 
The only difference is that it will actually create combinations where elements 
do repeat.
"""
from itertools import combinations_with_replacement

for item in combinations_with_replacement("WXYZ", 2):
    print("".join(item))


"""
product(*iterables, repeat=1)

The itertools package has a neat little function for creating Cartesian products 
from a series of input iterables.
"""
from itertools import product

arrays = [(-1, 1), (-3, 3), (-5, 5)]
cp = list(product(*arrays))
print(cp)

"""
permutations

The permutations sub-module of itertools will return successive r length 
permutations of elements from the iterable we give it. Much like the combinations 
function, permutations are emitted in lexicographic sort order. 
"""
from itertools import permutations

for item in permutations("WXYZ", 2):
    print("".join(item))
