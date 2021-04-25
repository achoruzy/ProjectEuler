# Copyright (c) 2021 Arkadiusz Choruży
# License: N/A

# ------------------------------------

# PROBLEM 60 Prime pair sets

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# ----------- PSEUDOCODE -------------

# generate primes
# check if previous and next primes concatenate into another prime in both ways
# find set of 5 such primes able to concatenate into primes between
# find sum oft such lowest set

# -------------- CODE ----------------
from math import sqrt


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


def prime_generator() -> int:
    """ Generates consecutive primes. """
    yield 2
    counter = 3
    while True:
        if_prime = is_prime(counter)
        if if_prime:
            yield counter
        counter += 2


def is_concatenate_to_prime(prime_1: int, prime_2: int) -> bool:
    """ Checks if two primes may be concatenated into another two primes in form prime_1prime_2 and prime_2prime_1. """
    connected_primes_12 = int(str(prime_1) + str(prime_2))
    if not is_prime(connected_primes_12):
        return False

    connected_primes_21 = int(str(prime_2) + str(prime_1))
    if not is_prime(connected_primes_21):
        return False

    return True


def prime_list_conc(lenght: int, prime_num: int) -> list:
    """Returns a list of primes that concatenate between them into another primes.
    Returned list has size of input length.
    prime_num is to assign with consecutive prime started from 3 (first) to start with"""
    gen = prime_generator()

    for i in range(prime_num):
        next(gen)

    first_prime = next(gen)
    result_list = [first_prime]

    while len(result_list) < lenght:
        num = next(gen)
        ok = True
        for i in result_list:
            if not is_concatenate_to_prime(num, i):
                ok = False
                break

        if ok:
            result_list.append(num)

    return result_list


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
    assert is_prime(958572) == False
    assert is_prime(958577) == True


def test_prime_generator():
    gen = prime_generator()
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 7
    assert next(gen) == 11


def test_is_concatenate_to_prime():
    num1 = 109
    num2 = 673
    result = is_concatenate_to_prime(num1, num2)
    assert result == True
    assert is_concatenate_to_prime(44, 22) == False


def test_prime_list_conc():
    assert prime_list_conc(lenght=2, prime_num=1) == [3, 7]
    assert prime_list_conc(lenght=3, prime_num=1) == [3, 7, 109]
    assert prime_list_conc(lenght=4, prime_num=1) == [3, 7, 109, 673]


# --------------- RUN ---------------
if __name__ == '__main__':
    first_prime = 8
    how_many = 4

    result = prime_list_conc(lenght=how_many, prime_num=first_prime)

    print('Result list:', result)
    print('Sum of result list = ', sum(result))


# ------------ RESULT -------------
