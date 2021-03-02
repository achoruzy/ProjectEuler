# PROBLEM 41 Pandigital prime

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?


# ----------- PSEUDOCODE -------------
# starting on the highest pandigital
# go through down
# first found is the result


# -------------- CODE ----------------
from math import factorial, sqrt


def pandigital(position: int, ran: int) -> int:
    """ Function returns integer number from given position from combinations of given range digits. """
    digit_list = [n for n in range(ran, 0, -1)]
    help_list = digit_list.copy()
    result_list = []
    result_str = ''
    num_of_solutions = factorial(len(digit_list))
    while len(help_list) > 0:
        range_size = num_of_solutions // len(help_list)
        list_dig_within = (position-1) // range_size
        num_of_solutions //= len(help_list)
        position -= (list_dig_within * range_size)
        result_list.append(help_list.pop(list_dig_within))

    for i in result_list:
        result_str += str(i)

    return int(result_str)


def is_prime(num: (int, str)) -> bool:
    """ Checks if the number is prime"""
    num = int(num)

    if num == 2:
        return True

    if num % 2 == 0 or num in (0, 1):
        return False
    elif num == 3:
        return True

    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False

    return True

# -------------- TESTS ---------------


def test_pandigital():
    # given
    pos = 1
    # when
    result = pandigital(1, 9)
    # then
    assert result == 987654321
    assert pandigital(362880, 9) == 123456789
    assert type(pandigital(7643, 8)) == int


def test_is_prime():
    # given
    num_1 = 3797
    num_2 = 888
    # when
    result_1 = is_prime(num_1)
    result_2 = is_prime(num_2)
    # then
    assert result_1 == True
    assert result_2 == False
    assert type(is_prime(3456)) == bool
    assert is_prime(1) == False
    assert is_prime(3) == True
    assert is_prime(55) == False


# --------------- RUN ---------------
if __name__ == '__main__':
    for i in range(9, 0, -1):
        for j in range(1, factorial(i)+1):
            num = pandigital(j, i)
            if is_prime(num):
                print(num)
                break


# ------------ RESULT -------------

# 7652413
