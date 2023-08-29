"""
the namedtuple class from the collection module which we can use to replace
Python’s tuple. Of course, the namedtuple is not a drop-in replacement as we
will see soon. We have seen some programmers use it like a struct. If we haven’t
used a language with a struct in it, then that needs a little explanation.
A struct is basically a complex data type that groups a list of variables under
one name.
"""
from collections import namedtuple


def namedtuple_func():
    Parts = namedtuple("Parts", "id_num desc cost amount")
    auto_parts = Parts(id_num="1234", desc="Ford Engine", cost=1200.00, amount=10)
    print(auto_parts.id_num)


def normal_tuple():
    auto_parts = ("1234", "Ford Engine", 1200.00, 10)
    print(auto_parts[0])

    id_num, desc, cost, amount = auto_parts
    print(id_num)


def dict_into_obj():
    Parts = {"id_num": "1234", "desc": "Ford Engine", "cost": 1200.00, "amount": 10}
    parts = namedtuple("Parts", Parts.keys())  # (**Parts)
    print(parts)
    auto_parts = parts(**Parts)
    print(auto_parts)


if __name__ == "__main__":
    namedtuple_func()
    normal_tuple()
    dict_into_obj()
