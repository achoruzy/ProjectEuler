# Copyright (c) 2021 Arkadiusz Choruży
# License: N/A

# ------------------------------------

# PROBLEM 60 Prime pair sets

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# ----------- PSEUDOCODE -------------

#

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


# -------------- TESTS ---------------

def test_():
    # given
    # when
    # then
    pass


# --------------- RUN ---------------
if __name__ == '__main__':
    pass


# ------------ RESULT -------------
