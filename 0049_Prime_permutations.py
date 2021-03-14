# PROBLEM 49 Prime permutations

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

# ----------- PSEUDOCODE -------------

# go from 1000 to 3390
# get sum of num + 3330 and + 6660
# check if have same digits
# check if all are primes

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


def check_permutations(num: int, adder: int) -> bool:
    num_2 = num + adder
    num_3 = num_2 + adder
    # string var
    num_str = {i for i in str(num)}
    num_2_str = {i for i in str(num_2)}
    num_3_str = {i for i in str(num_3)}
    # logic
    if num_str == num_2_str == num_3_str:
        for i in [num, num_2, num_3]:
            if not is_prime(i):
                return False
    else:
        return False
    return True


def main():
    for num in range(1001, 9997):
        if is_prime(num):
            limit = int((9999-num)/2)+1
            for adder in range(1000, limit):
                if check_permutations(num, adder):
                    print(num, num+adder, num+adder+adder, ' adder:', adder)

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


def test_check_permutations():
    # given
    num = 1487
    adder = 3330
    # when
    result = check_permutations(num, adder)
    # then
    assert result == True
    assert check_permutations(4897, 1234) == False


# --------------- RUN ---------------
if __name__ == '__main__':
    main()


# ------------ RESULT -------------
