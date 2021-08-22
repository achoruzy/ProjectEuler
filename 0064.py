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


def closest_square(num: int) -> int:
    """Finds closest lower ideal square.
    """
    closest_square = int(num**0.5)
    return closest_square


# -------------- TESTS ---------------

def test_closest_square():
    # given
    # when
    # then
    assert 1 == closest_square(1)
    assert 1 == closest_square(2)
    assert 1 == closest_square(3)
    assert 2 == closest_square(5)
    assert 10 == closest_square(108)


# --------------- RUN ---------------
if __name__ == '__main__':
    pass


# ------------ RESULT -------------
