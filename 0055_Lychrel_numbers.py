# PROBLEM 55 Lychrel numbers

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
# How many Lychrel numbers are there below ten-thousand?

# ----------- PSEUDOCODE -------------

# go in range 10 to 10000
# check if number is palindrome
#   if it is add 1 if not add to it it's reversed version then check the sum if is palindrome
#   check such for not more than 50 iterations

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


def is_palindrome(num: int) -> bool:
    """Function checks if a number is palindrome - num is same as it's reversed version"""
    num_str = str(num)
    reversed_num = num_str[::-1]

    if num_str == reversed_num:
        return True
    return False


def reversed_int(num: int) -> int:
    """ Returns reversed integer"""
    num_str = str(num)
    reversed_num = num_str[::-1]
    reversed_int = int(reversed_num)
    return reversed_int


def lychrel_num(num: int, iteration_counter=0) -> bool:
    """Checks if num is Lychrel number"""

    if iteration_counter == 51:
        return True

    reversed_num = reversed_int(num)
    next_num = num + reversed_num
    iteration_counter += 1

    is_num_palindrome = is_palindrome(next_num)
    if is_num_palindrome:
        return False

    return lychrel_num(next_num, iteration_counter)


def main_function():
    counter = 0
    for i in range(1, 10000):
        lychel_check = lychrel_num(i)
        if lychel_check:
            counter += 1

    return counter

# -------------- TESTS ---------------


def test_is_palindrome():
    # given
    num = 6776
    # when
    result = is_palindrome(num)
    # then
    assert result == True
    assert is_palindrome(4567) == False


def test_reversed_int():
    num = 189
    result = reversed_int(num)
    assert result == 981


def test_lychrel_num():
    num = 349
    result = lychrel_num(num)
    assert result == False
    assert lychrel_num(196) == True
    assert lychrel_num(4994) == True


# --------------- RUN ---------------
if __name__ == '__main__':
    print(main_function())


# ------------ RESULT -------------

# 249
