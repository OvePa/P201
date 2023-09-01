"""
Creating an Alias using typing module
The other thing that we thought was interesting is that we can create an Alias.
"""
Animal = str


def zoo(animal: Animal, number: int) -> None:
    print("The zoo has %s %s" % (number, animal))


if __name__ == "__main__":
    zoo("Zebras", 10)
