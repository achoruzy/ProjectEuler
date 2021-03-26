# PROBLEM 53 Combinatory selections

# https://projecteuler.net/problem=53


# ----------- PSEUDOCODE -------------

#

# -------------- CODE ----------------
from time import time
from math import factorial


def timing(func):
    """ Decorator function for calculating working time of another function."""
    def wrapper(*args, **kwargs):
        time_1 = time()
        return_var = func(*args, **kwargs)
        time_2 = time()
        print('Function worked: ', str(time_2-time_1)[:5], ' sec.')
        return return_var
    return wrapper()


def combinatronics(n: int, r: int) -> int:
    if r > n:
        raise Exception('r can\'t be higher than n!')

    result = (factorial(n))/(factorial(r)*(factorial(n-r)))
    return result


def main_func() -> int:
    counter = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            check = combinatronics(n, r)
            if check > 1000000:
                counter += 1

    return print(counter)

    # -------------- TESTS ---------------


def test_combinatronics():
    # given
    n = 23
    r = 10
    # when
    result = combinatronics(n, r)
    # then
    assert result == 1144066
    assert combinatronics(5, 3) == 10


# --------------- RUN ---------------
if __name__ == '__main__':
    main_func()


# ------------ RESULT -------------
