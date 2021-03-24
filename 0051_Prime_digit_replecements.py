# PROBLEM 51 Prime digit replacements

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.


# ----------- PSEUDOCODE -------------

# go over primes starting from 60000
#   for each prime go for possible swaps
#       swap with 0 to 9


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


def eight_primes(num: int, dig: str, limit=8) -> bool:
    """Checks if a num has 8 primes when digits replaced."""
    counter = 0
    primes = ()
    num_str = str(num)
    for i in range(0, 10):
        i_str = str(i)
        # new_num = num_str[0] + num_str[1:-1].replace(dig, i_str) + num_str[-1]
        new_num = num_str.replace(dig, i_str)
        new_num_int = int(new_num)
        if is_prime(new_num_int) and len(str(new_num_int)) == len(num_str):
            primes += (new_num_int,)
            counter += 1

    if counter >= limit:
        print(primes)
        return True
    return False


def check_conditions(num: int, limit=8) -> bool:
    """ Checks if problem conditions are fulfilled for a number."""
    conditions = False
    if is_prime(num):
        num_str = str(num)
        trimmed_num = num_str[1:-1]
        for dig in range(0, 9):
            dig_str = str(dig)
            if trimmed_num.count(dig_str) > 1:
                conditions = eight_primes(num, dig_str, limit)
    if conditions:
        return True
    return False


def main_func() -> int:
    """ Main problem solving function. """
    result = 0

    counter = 60000
    while True:
        if check_conditions(counter):
            result = counter
            break
        counter += 1

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
    assert is_prime(958572) == False
    assert is_prime(958577) == True


def test_eight_primes():
    # given
    num = 56003
    dig = '0'
    limit = 7
    # when
    result = eight_primes(num, dig, limit)
    # then
    assert type(result) == bool
    assert result == True
    assert eight_primes(56004, '0') == False


def test_check_conditions():
    # given
    num = 56003
    limit = 7
    # when
    result = check_conditions(num, limit)
    # then
    assert type(result) == bool
    assert result == True
    assert check_conditions(60000) == False


# --------------- RUN ---------------
if __name__ == '__main__':
    result = main_func()
    print(result)


# ------------ RESULT -------------

# (121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393)
# 121313
