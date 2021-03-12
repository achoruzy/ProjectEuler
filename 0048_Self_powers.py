# PROBLEM 48 Self powers

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# ----------- PSEUDOCODE -------------

# go over nums 1 to 1000
#   # add each next number to result
#   # check last 10 digs from string version of result

# -------------- CODE ----------------
from time import time


def timing(func):
    """ Decorator function for calculating working time of another function."""
    def wrapper(*args, **kwargs):
        time_1 = time()
        return_var = func(*args, **kwargs)
        time_2 = time()
        print('Function worked: ', str(time_2-time_1)[:5], ' sec.')
        return return_var
    return wrapper()


def sum_of_self_powers(in_range: int) -> int:
    """ Returns sum of squares of consecutive integers up to in_range."""
    result_sum = 0
    generator = (i**i for i in range(1, in_range+1))

    for i in generator:
        result_sum += i

    return result_sum


def get_last_10_digs(num: int) -> str:
    str_num = str(num)
    return str_num[-10:]


# -------------- TESTS ---------------


def test_sum_of_self_powers():
    # given
    in_range = 10
    # when
    result = sum_of_self_powers(in_range)
    # then
    assert result == 10405071317


def test_get_last_10_digs():
    # given
    num = 77770987654321
    # when
    result = get_last_10_digs(num)
    # then
    assert result == '0987654321'


# --------------- RUN ---------------
if __name__ == '__main__':
    number = sum_of_self_powers(1000)
    digs = get_last_10_digs(number)
    print(digs)


# ------------ RESULT -------------
# 9110846700
