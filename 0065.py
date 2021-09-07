# PROBLEM 65

#


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
