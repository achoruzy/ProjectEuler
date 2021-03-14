# PROBLEM 50 Consecutive prime sum

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?


# ----------- PSEUDOCODE -------------

# go from 1
#   add each next prime to the last sum
#   store the sume and number of adders if bigger than previous one
#   up to sum >= 1mln

# -------------- CODE ----------------
from math import sqrt
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


def is_prime(num: int) -> bool:
    """ Checks if num is prime number."""
    if num in [0, 1]:
        return False
    if num in [2, 3, 5, 7]:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


def main():
    # num = 1

    biggest_prime = 0
    biggest_adders = 0

    for num in range(1, 50):
        prime_sum = 0
        adders = 0
        while prime_sum < 1000000:
            if is_prime(num):
                prime_sum += num
                adders += 1
                if is_prime(prime_sum) and prime_sum < 1000000:
                    if adders > biggest_adders:
                        biggest_prime = prime_sum
                        biggest_adders = adders
            num += 1
    print(biggest_prime, biggest_adders)


# -------------- TESTS ---------------


def test_is_prime():
    # given
    num = 17
    # when
    result = is_prime(num)
    # then
    assert type(result) == bool
    assert result == True
    assert is_prime(5777) == False
    assert is_prime(958577) == True


# --------------- RUN ---------------
if __name__ == '__main__':
    main()

# ------------ RESULT -------------
