# PROBLEM 64 Odd period square roots

# https://projecteuler.net/problem=64


# ----------- PSEUDOCODE -------------

# get next number A for square root
# check what is closest ideal square root SQR for number A
# make number in form SQR + SQRT(A) - SQR
# append SQR to the list of check digits
# check if fractions in list are repeatable -> if yes and if odd number of then +1 to result

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


def total_part(num: float or int) -> int:
    """Finds total part of irrational number.
    """
    closest_square = int(sqrt(num))
    return closest_square


def one_divide_by_irrational(irr_prt: int, tot_prt: int) -> float:
    """Finds irrational (fraction) part of irrational number.
    """
    result = (sqrt(irr_prt) + tot_prt)/(irr_prt - tot_prt**2)
    return abs(result)


def continued_fraction(num: int, lenght: int) -> list:
    result_list = []

    sqr = sqrt(num)

    total = total_part(num)
    result_list.append(total)

    irrational = sqr - total

    while len(result_list) < lenght:

        irrational_under_one = one_divide_by_irrational(irrational, total)

        total = total_part(irrational_under_one)  # tu jest blad
        result_list.append(total)
        print(total, irrational_under_one)

        irrational = irrational_under_one - total

    return result_list

# -------------- TESTS ---------------


def test_total_part():
    # given
    # when
    # then
    assert 1 == total_part(1)
    assert 1 == total_part(2)
    assert 1 == total_part(3)
    assert 2 == total_part(5)
    assert 10 == total_part(108)


def test_one_divide_by_irrational():
    pass


def test_continued_fraction():
    pass


# --------------- RUN ---------------
if __name__ == '__main__':
    print(continued_fraction(2, 4))


# ------------ RESULT -------------
