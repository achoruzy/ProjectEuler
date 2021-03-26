# PROBLEM 52 Permuted multiples

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# ----------- PSEUDOCODE -------------

# go over nums startet from 123456
#   check num * 1 to 6
#   check if nums contains same digits

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


def same_digits(num1: int, num2: int) -> bool:
    set1 = {i for i in str(num1)}
    set2 = {i for i in str(num2)}
    if len(set1) == len(str(num1)):
        return set1 == set2
    return False


def main_func():
    counter = 123456

    while True:
        all_ok = 1
        for i in range(2, 7):
            multiplied = counter * i
            if not same_digits(counter, multiplied):
                break
            else:
                all_ok += 1
        if all_ok == 6:
            print(counter)
            break
        counter += 1


# -------------- TESTS ---------------

def test_same_digits():
    # given
    num1 = 23
    num2 = 32
    # when
    result = same_digits(num1, num2)
    # then
    assert result == True


# --------------- RUN ---------------
if __name__ == '__main__':
    main_func()


# ------------ RESULT -------------
# 142857
