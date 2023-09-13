import cProfile

cProfile.run("[x for x in range(1500)]")

"""
Let’s break this down a bit. The first line shows that there were four function 
calls. The next line tells us how the results are ordered. According to the 
documentation, standard name refers to the far right column. There are a number 
of columns here.

* ncalls is the number of calls made.
* tottime is the total time spent in the given function.
* percall refers to the quotient of tottime divided by ncalls.
* cumtime is the cumulative time spent in this and all subfunctions. It’s even 
    accurate for recursive functions!
* The second percall column is the quotient of cumtime divided by primitive calls.
* filename:lineno(function) provides the respective data of each function.

We can call cProfile on the command line in much the same way as we did with 
the timeit module. The main difference is that we would pass a Python script to 
it instead of just passing a snippet.
"""

# cmd
# python3 -m cProfile cprofile_bi.py
