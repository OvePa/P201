"""
Type hinting is kind of declaring our function’s arguments to have a certain type.
However the type hinting is not binding. It’s just a hint, so there’s nothing
preventing the programmer from passing something they shouldn’t. This is Python
after all. We can read the type hinting specification in PEP 484 or we can just
read the theory behind it in PEP 483.
"""


def some_function(number: int, name: str) -> None:
    print("%s entered %s" % (name, number))


print(some_function(13, "Mike"))

"""
This means that some_function expects two arguments where the first is an 
integer and the second is a string. It should also be noted that we have hinted
that this function returns None.
"""


def process_data(my_list: list, name: str) -> bool:
    return name in my_list


if __name__ == "__main__":
    my_list = ["Mike", "Nick", "Toby"]
    print(process_data(my_list, "Mike"))
    print(process_data(my_list, "John"))
