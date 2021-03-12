# PROBLEM 47 Distinct primes factors

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


# ----------- PSEUDOCODE -------------

# go over int numbers, each next +1
#   for each num divide it by consecutive primes
#   if possible to divide it by 4 primes without rest then +1 to counter
#   if not then counter = 0
# when counter = 4 the first num from list is result

# -------------- CODE ----------------
from time import time
from math import sqrt


def timing(func):
    """ Decorator function for calculating working time of another function."""
    def wrapper(*args, **kwargs):
        time_1 = time()
        return_var = func(*args, **kwargs)
        time_2 = time()
        print('Function worked: ', str(time_2-time_1)[:5], ' sec.')
        return return_var
    return wrapper()


def is_prime(num: int) -> bool:
    """ Checks if num is prime number."""
    if num in [0, 1]:
        return False
    if num in [2, 3, 5, 7]:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


def distinct_primes_4(num: int) -> bool:
    """ Checks if the num can be divided by 4 different primes (that also may repeat but it's not counted into)."""
    check = set()
    rng_end = int((num/2))+1
    rng_start = 2

    for i in range(rng_start, int(rng_end/2)+1):
        if num % i == 0:
            if is_prime(i):
                check.add(i)
                num = num // i

    if len(check) == 4:
        return True
    else:
        return False


@timing
def result_func() -> list:
    result = []
    counter_4 = 0
    num = 210
    last_num = 0
    while counter_4 < 4:
        if distinct_primes_4(num):
            result.append(num)
            counter_4 += 1
        else:
            counter_4 = 0
            result.clear()
        last_num = num
        num += 1

    return result


# -------------- TESTS ---------------

def test_is_prime():
    # given
    num = 17
    # when
    result = is_prime(num)
    # then
    assert type(result) == bool
    assert result == True
    assert is_prime(5777) == False


def test_distinct_primes_4():
    # given
    num = 210
    # when
    result = distinct_primes_4(num)
    # then
    assert result == True


# --------------- RUN ---------------
if __name__ == '__main__':
    print(result_func())


# ------------ RESULT -------------
#[134043, 134044, 134045, 134046]
