# PROBLEM 0057 Square root convergents

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# By expanding this for the first four iterations, we get:

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
# https://projecteuler.net/problem=57

# ----------- PSEUDOCODE -------------

# go over to 1000
# count fractions for each iteration
# compare numerator and denominator

# -------------- CODE ----------------

import pytest as pt


def a_longer_than_b(a: int, b: int) -> bool:
    """Returns True if num a has more digits than num b."""
    if type(a) != int or type(b) != int:
        raise TypeError('a or b number is not integer type!')

    a_str = str(a)
    b_str = str(b)

    if len(a_str) > len(b_str):
        return True

    return False


def fraction_even_denominator(num: list, num_to_even: list) -> list:
    """Returns number reduced to a common denominator taken from num_to_even."""
    result = num
    for i in range(0, 2):
        result[i] *= num_to_even[1]

    return result


def square_root_iterator(span: int) -> float:
    """Yields next decimal iterations of square root of 2."""
    counter = 0

    x = 1
    while counter <= span:
        sq_root_iteration_func = (1+(1/(1 + x)))
        yield sq_root_iteration_func
        x = sq_root_iteration_func
        counter += 1


def square_root_fraction_iterator(span: int) -> list:
    """Square root of 2 iteration generator, returns a list [numerator, denominator].
    Basic function is 1 + (1/(1 + x)) where x is equal to the last result."""
    counter = 1

    x = [1, 1]

    while counter <= span:
        # fraction part calculation
        fraction_part = [0, 0]
        fraction_one = fraction_even_denominator([1, 1], x)

        fraction_part[0] = x[1]
        fraction_part[1] = fraction_one[0] + x[0]

        # final calculation
        result = [0, 0]

        fraction_upside = fraction_part[::-1]

        result_one = fraction_even_denominator([1, 1], fraction_part)
        result[0] = result_one[0] + fraction_part[0]
        result[1] = fraction_part[1]

        yield result

        x = result

        counter += 1


# -------------- TESTS ---------------


def test_a_longer_than_b():
    # given
    a = 234
    b = 9876
    # when
    result = a_longer_than_b(a, b)
    # then
    assert result == False
    assert a_longer_than_b(b, a) == True
    with pt.raises(TypeError):
        a_longer_than_b(12, 1.32)


def test_square_root_iterator():
    span = 2
    result = square_root_iterator(span)

    assert next(result) == 1.5
    assert next(result) == 1.4


def test_fraction_even_denominator():
    num = [1, 1]
    num_even_to = [1, 2]
    result = fraction_even_denominator(num, num_even_to)
    assert result == [2, 2]
    assert fraction_even_denominator([1, 1], [54, 76]) == [76, 76]


def test_square_root_fraction_iterator():
    span = 2
    result = square_root_fraction_iterator(span)

    assert next(result) == [3, 2]
    assert next(result) == [7, 5]


# --------------- RUN ---------------
if __name__ == '__main__':
    counter = 0
    for i in square_root_fraction_iterator(1000):
        numerator_len = len(str(i[0]))
        denominator_len = len(str(i[1]))
        if numerator_len > denominator_len:
            counter += 1
    print(counter)

# ------------ RESULT -------------

# 153
