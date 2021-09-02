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


def continued_fraction(num: int, lenght: int) -> list:
    """Generates list notation for continued fraction representations of (irrational) square roots.
    """
    result_list = []

    sqr = sqrt(num)

    # First digit
    total = total_part(num)
    result_list.append(total)

    irrational = sqr - total

    # Next digits
    while len(result_list) < lenght:

        irrational_under_one = irrational**(-1)

        total = int(irrational_under_one)
        result_list.append(total)
        print(total, irrational_under_one)

        irrational = irrational_under_one - total

    return result_list


def count_period(list_to_check: list) -> int:
    """Counts quantity of perioded numbers in list.
    """
    del list_to_check[0]
    list_len = len(list_to_check)

    for start in range(0, int(list_len/4)):
        stop = start + 1

        while stop <= list_len/2:
            ss_difference = stop - start
            base = list_to_check[start: stop]

            for i in range(1, 5):
                check = list_to_check[start+ss_difference*i:
                                      stop+ss_difference*i]
                if check != base:
                    break

                return ss_difference

            stop += 1

    return 0


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


def test_continued_fraction():
    assert [4, 1, 3, 1, 8, 1, 3, 1, 8, 1] == continued_fraction(23, 10)


def test_count_period():
    check_list = [4, 1, 3, 1, 8, 1, 3, 1, 8, 1]
    assert 4 == count_period(check_list)

    check_list_2 = continued_fraction(23, 100)
    assert 4 == count_period(check_list_2)


# --------------- RUN ---------------
if __name__ == '__main__':

    # ------------ RESULT -------------
