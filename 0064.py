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
    closest_square = int(num**0.5)
    return closest_square


def irrational_num_rest(irrational_prt: int, total_prt: int) -> float:
    result = 1 / (irrational_prt**0.5 - total_prt)
    return int(result)


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


def test_irrational_num_rest():
    assert 2 == irrational_num_rest(2, 1)
    assert 1 == irrational_num_rest(23, 4)


# --------------- RUN ---------------
if __name__ == '__main__':
    pass


# ------------ RESULT -------------
