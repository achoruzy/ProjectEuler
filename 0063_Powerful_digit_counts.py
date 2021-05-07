# PROBLEM xx xxx

# The number


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


def main():
    counter = 0
    num = 0
    while True:
        num += 1

        power = 0
        while True:
            power += 1
            result = num ** power
            length = len(str(result))
            if length == power:
                counter += 1
                continue
            elif power > length:
                break
            elif result % 100 == 0:
                return counter


# -------------- TESTS ---------------

def test_():
    # given
    # when
    # then
    pass


# --------------- RUN ---------------
if __name__ == '__main__':
    print(main())


# ------------ RESULT -------------
# 49
