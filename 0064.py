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

    m = 0
    d = 1
    a = a0 = int(sqrt(num))

    result_list.append(a)

    count = 0
    while count < lenght-1:
        m = d * a - m
        d = (num - m**2)/d
        a = int((a0 + m)/d)

        result_list.append(a)

        count += 1

    return result_list


def count_period(list_to_check: list) -> int:
    """Counts quantity of perioded numbers in list.
    """

    count = 0
    for i in list_to_check[1:]:
        count += 1
        if i == 2*list_to_check[0]:
            break

    return count


def good_root(num: int) -> bool:
    """Checks if root of number is rational.
    """
    sqroot = int(sqrt(num))
    square = sqroot**2

    if square == num:
        return True

    return False


def main(check_range: int) -> int:

    odd_counter = 0

    for i in range(2, check_range+1):

        # Remove good roots
        if good_root(i):
            continue

        # Counting odds
        checked_root = continued_fraction(i, 1000)
        counted_period = count_period(checked_root)
        if counted_period % 2 != 0:
            odd_counter += 1
            # print(i, counted_period, odd_counter)

    return odd_counter

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
    check_list = continued_fraction(10, 100)
    assert 1 == count_period(check_list)

    check_list_2 = continued_fraction(23, 100)
    assert 4 == count_period(check_list_2)

    check_list_3 = continued_fraction(7, 100)
    assert 4 == count_period(check_list_3)


def test_good_root():
    assert True == good_root(9)


# --------------- RUN ---------------
if __name__ == '__main__':
    print(main(10000))


# ------------ RESULT -------------
