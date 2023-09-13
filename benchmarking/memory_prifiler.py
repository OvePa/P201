# pip3 install memory_profiler
# cmd
# python3 -m memory_profiler memo_prof.py
# it can be used to create full memory usage reports over time instead of
# line-by-line.
# mprof run memo_prof.py
"""
The memory_profiler module can be used for monitoring memory consumption in a
process or we can use it for a line-by-line analysis of the memory consumption
of our code.
"""
from memory_profiler import profile


@profile
def mem_func():
    t_range = 1000
    import random

    range_num1 = [random.randint(1, 10) for i in range(t_range)]
    range_num2 = [random.randint(1, 10) for i in range(t_range)]
    sum_range = [range_num1[i] + range_num2[i] for i in range(t_range)]
    total_of_ranges = sum(sum_range)
    print(total_of_ranges)


if __name__ == "__main__":
    mem_func()
