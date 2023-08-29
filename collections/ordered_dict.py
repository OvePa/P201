"""
Python’s collections module has another great subclass of dict known as
OrderedDict. As the name implies, this dictionary keeps track of the order of
the keys as they are added.
"""

from collections import OrderedDict, Counter

Counter("superfluous")
counter = Counter("superfluous")
print(counter)
d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
print(d)

# There are times when we will need to loop over the keys of our dictionary in
# a specific order.
d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
keys = d.keys()
print(keys)


keys = sorted(keys)
print(keys)


for key in keys:
    print(key, d[key])

# OrderedDict
d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
new_d = OrderedDict(sorted(d.items()))
print(new_d)

for key in new_d:
    print(key, new_d[key])

for key in reversed(new_d):
    print(key, new_d[key])
