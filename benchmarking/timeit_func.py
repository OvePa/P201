# simple_func2.py
def my_function():
    try:
        1 / 0
    except ZeroDivisionError:
        pass


if __name__ == "__main__":
    import timeit

    setup = "from __main__ import my_function"
    print(timeit.timeit("my_function()", setup=setup))


"""
Here we check to see if the script is being run directly (i.e. not imported). 
If it is, then we import timeit, create a setup string to import the function 
into timeit’s namespace and then we call timeit.timeit. Please note that we 
pass a call to the function in quotes, then the setup string. And that’s really 
all there is to it!
"""
# python shell
# python -m timeit -s 'text="hello world"'
# python -m timeit -s "\[ord(x) for x in 'abcdfghi'\]"
