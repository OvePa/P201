from collections import Counter

print(Counter("superfluous"))

counter = Counter("superfluous")
print(counter["u"])
# we can call elements which will be an iterator over the elements that are in
# the dictionary, but in an arbitrary order.
print(list(counter.elements()))

# We can ask the Counter what the most common items are by passing in a number
# that represents the top recurring “n” items.
print(counter.most_common(1))

# The subtract method accepts an iterable or a mapping and then uses that
# argument to subtract.

counter_one = Counter("superfluous")
print("Counter One: ", counter_one)

counter_two = Counter("super")
print("Counter One minus super: ", counter_one.subtract(counter_two))

print(counter_one)
