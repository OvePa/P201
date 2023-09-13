# pip3 install line_profiler
# cmd
# kernprof -l silly_functions.py

# silly_functions.py
import time


# @profile
def fast_function():
    print("I'm a fast function!")


# @profile
def slow_function():
    time.sleep(2)
    print("I'm a slow function")


if __name__ == "__main__":
    fast_function()
    slow_function()

"""
So now we have two decorated functions that are decorated with something that 
isn’t imported. If we actually try to run this script as it is, we will get a 
NameError because “profile” is not defined. So always remember to remove your 
decorators after you have profiled your code!
"""
# cmd to view results
# 1 python3 -m line_profiler silly_functions.py.lprof
# 2 kernprof -l -v silly_functions.py
