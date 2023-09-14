def my_func(a, b):
    global x
    print("global1", x)
    x = 5
    print("global2", x)


if __name__ == "__main__":
    x = 10
    my_func(1, 2)
    print(x)
