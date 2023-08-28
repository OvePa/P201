"""
The defaultdict is a subclass of Python’s dict that accepts a default_factory
as its primary argument. The default_factory is usually a Python type, such as
int or list, but we can also use a function or a lambda.
"""
from collections import defaultdict


def normal_dic(words):
    reg_dict = {}
    for word in words:
        if word in reg_dict:
            reg_dict[word] += 1
        else:
            reg_dict[word] = 1

    print(reg_dict)


def default_dict(words):
    d = defaultdict(int)
    for word in words:
        d[word] += 1

    print(d)


def normal_list_type(lst):
    reg_dict = {}
    for acct_num, value in lst:
        if acct_num in reg_dict:
            reg_dict[acct_num].append(value)
        else:
            reg_dict[acct_num] = [value]

    print(reg_dict)


def default_dict_list_type(lst):
    d = defaultdict(list)
    for acct_num, value in lst:
        d[acct_num].append(value)

    print(d)


def lambda_default_factory():
    # it will assign ‘Monkey’ as the default value to any key.
    animal = defaultdict(lambda: "Monkey")
    animal["Sam"] = "Tiger"

    print(animal["Nick"])

    print(animal)


if __name__ == "__main__":
    sentence = "The red for jumped over the fence and ran to the zoo for food"
    words = sentence.split(" ")
    normal_dic(words)
    default_dict(words)

    my_list = [
        (1234, 100.23),
        (345, 10.45),
        (1234, 75.00),
        (345, 222.66),
        (678, 300.25),
        (1234, 35.67),
    ]
    normal_list_type(my_list)
    default_dict_list_type(my_list)

    lambda_default_factory()
