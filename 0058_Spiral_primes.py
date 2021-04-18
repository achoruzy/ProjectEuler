# PROBLEM 58 Spiral Primes

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

# ----------- PSEUDOCODE -------------

# generate spiral numbers
# check if primes
# update % of primes
# stop when % <= 10%

# -------------- CODE ----------------
from math import sqrt


def spiral_generator() -> int:
    """Generates diagonal numbers for square spiral."""
    corner_counter = 0
    spiral_counter = 1
    adder_const = 2
    last = 1

    yield 1

    while True:

        if corner_counter == 4:
            spiral_counter += 1
            corner_counter = 0

        num = last + (adder_const*spiral_counter)
        yield num
        last = num
        corner_counter += 1


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


def main_func():
    counter_all = 0
    counter_primes = 0
    ratio = 1

    for i in spiral_generator():
        prime_check = is_prime(i)
        if prime_check:
            counter_primes += 1
        counter_all += 1

        if counter_all > 1:
            ratio = counter_primes / counter_all

        if ratio <= 0.1:
            num_of_layers = (counter_all - 1) / 4
            spiral_size = 1 + num_of_layers * 2
            return int(spiral_size + 1)


# -------------- TESTS ---------------


def test_spiral_generator():
    gen = spiral_generator()
    assert next(gen) == 1
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 7
    assert next(gen) == 9
    assert next(gen) == 13
    assert next(gen) == 17
    assert next(gen) == 21


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


# --------------- RUN ---------------
if __name__ == '__main__':
    main = main_func()
    print(main)


# ------------ RESULT -------------
# 26241
