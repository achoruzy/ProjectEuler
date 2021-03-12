# PROBLEM 46 Goldbach's other conjecture

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# ----------- PSEUDOCODE -------------

# generate odd, non-prime numbers
# for above (num):
#   go over squared integers multilplied (i) by 2 as long as it is lower than num
#   check if num - i is prime
# the num with no prime found is the answer

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


def i_generator(stop: int) -> int:
    for i in range(1, stop-1):
        result = i*i*2
        if result >= stop-1:
            StopIteration
        else:
            yield result


def is_prime(num: int) -> bool:
    """ Checks if num is prime number."""
    if num in [0, 1]:
        return False
    if num in [2, 3, 5, 7]:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num/2)+1, 2):
        if num % i == 0:
            return False
    return True


def non_prime_odd_gen() -> int:
    num = 7
    while True:
        num += 2
        if is_prime(num):
            continue
        else:
            yield num


@timing
def result_func():
    for num in non_prime_odd_gen():
        check = True
        for i in i_generator(num):
            if i >= num:
                check = False
                break
            to_check = num - i
            if is_prime(to_check):
                check = False
                break
        if check:
            return print(num)

# -------------- TESTS ---------------


def test_i_generator():
    # given
    stop = 40
    # when
    result = []
    for i in i_generator(stop):
        result.append(i)
    # then
    assert result == [2, 8, 18, 32]


def test_is_prime():
    # given
    num = 17
    # when
    result = is_prime(num)
    # then
    assert type(result) == bool
    assert result == True
    assert is_prime(5777) == False


def test_non_prime_odd_gen():
    # given
    # when
    result = []
    stop = 4
    for i in non_prime_odd_gen():
        result.append(i)
        stop -= 1
        if stop == 0:
            break
    # then
    assert result == [9, 15, 21, 25]


# --------------- RUN ---------------
if __name__ == '__main__':

    result_func()


# ------------ RESULT -------------
# 5777
