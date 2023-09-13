# profhooks2.py
from profilehooks import timecall


@timecall
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

# cmd
# python3 -m profilehooks profhooks2.py