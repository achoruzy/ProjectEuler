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


def square_root_iterator(span: int) -> list:
    yield [3, 2]

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

    assert next(result) == [3, 2]
    assert next(result) == [7, 5]


# --------------- RUN ---------------
if __name__ == '__main__':
    pass


# ------------ RESULT -------------
