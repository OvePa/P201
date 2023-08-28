"""
According to the Python documentation, “deques are a generalization of stacks
and queues”. They are pronounced “deck” which is short for “double-ended queue”.
They are a replacement container for the Python list. Deques are thread-safe
and support memory efficient appends and pops from either side of the deque.
A list is optimized for fast fixed-length operations. A deque accepts a maxlen
argument which sets the bounds for the deque. Otherwise the deque will grow to
an arbitrary size. When a bounded deque is full, any new items added will cause
the same number of items to be popped off the other end.
"""
from collections import deque
import string


def get_last(filename, n=5):
    """
    Returns the last n lines from the file.
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print(f"Error opening the file {filename}")
        raise


if __name__ == "__main__":
    d = deque(string.ascii_lowercase)
    for letter in d:
        print(letter, end=",")
    d.append("bork")
    print("\n")
    print(d, end=",")

    print("\n")
    d.appendleft("test")
    print(d, end=",")

    print("\n")
    d.rotate(1)
    print(d, end=",")

    print("\n")
    result = get_last("test.txt")
    print(result)
