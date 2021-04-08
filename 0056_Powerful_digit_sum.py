# PROBLEM 56 Powerful digit sum

# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

# ----------- PSEUDOCODE -------------

# go inversed from a, b = 99 down
# check sum of digits a^b
# find max sum

# -------------- CODE ----------------
from time import time
from math import pow


def timing(func):
    """ Decorator function for calculating working time of another function."""
    def wrapper(*args, **kwargs):
        time_1 = time()
        return_var = func(*args, **kwargs)
        time_2 = time()
        print('Function worked: ', str(time_2-time_1)[:5], ' sec.')
        return return_var
    return wrapper()


def sum_of_digits(num: int) -> int:
    """ Returns sum of consecutive digits from of num."""
    sum_of_digs = 0

    num_str = str(num)
    for dig in num_str:
        dig_int = int(dig)
        sum_of_digs += dig_int

    return sum_of_digs


def main_func() -> int:

    max_sum = 0
    sum_for = [0, 0]

    for a in range(99, 21, -1):
        for b in range(99, 21, -1):
            power = a ** b
            digs_sum = sum_of_digits(power)
            if digs_sum > max_sum:
                max_sum = digs_sum
                sum_for = [a, b]

    return max_sum, sum_for


# -------------- TESTS ---------------

def test_sum_of_digits():
    num = 465573
    result = sum_of_digits(num)
    assert result == 30


# --------------- RUN ---------------
if __name__ == '__main__':
    main = main_func()
    print(main)


# ------------ RESULT -------------
# 972
