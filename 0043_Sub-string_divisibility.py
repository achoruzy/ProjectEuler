# PROBLEM 43 Sub-string divisibility

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.


# ----------- PSEUDOCODE -------------

#

# -------------- CODE ----------------
from math import factorial, sqrt


def pandigital(position: int) -> int:
    """ Function returns integer number from given position from combinations of given range digits. """
    digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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


def is_substring(num):
    num_str = str(num)
    if len(num_str) != 10:
        return False
    if int(num_str[1:4]) % 2 != 0:
        return False
    if int(num_str[2:5]) % 3 != 0:
        return False
    if int(num_str[3:6]) % 5 != 0:
        return False
    if int(num_str[4:7]) % 7 != 0:
        return False
    if int(num_str[5:8]) % 11 != 0:
        return False
    if int(num_str[6:9]) % 13 != 0:
        return False
    if int(num_str[7:10]) % 17 != 0:
        return False
    return True

# -------------- TESTS ---------------


def test_pandigital():
    # given
    pos = 1
    # when
    result = pandigital(1)
    # then
    assert result == 123456789
    assert pandigital(factorial(10)) == 9876543210
    assert type(pandigital(7643)) == int


def test_is_substring():
    # given
    num = 1406357289
    # when
    result = is_substring(num)
    # then
    assert result == True


# --------------- RUN ---------------
if __name__ == '__main__':
    result_list = []
    for pos in range(1, factorial(10)+1):
        num = pandigital(pos)
        if is_substring(num):
            print(num)
            result_list.append(num)
    print(sum(result_list))


# ------------ RESULT -------------
# 16695334890
