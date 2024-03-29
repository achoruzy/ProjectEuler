# PROBLEM 61 Cyclical figurate numbers

# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
# Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Square 	  	P4,n=n2 	  	1, 4, 9, 16, 25, ...
# Pentagonal 	  	P5,n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	P6,n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
# Heptagonal 	  	P7,n=n(5n−3)/2 	  	1, 7, 18, 34, 55, ...
# Octagonal 	  	P8,n=n(3n−2) 	  	1, 8, 21, 40, 65, ...

# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

#     The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
#     Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
#     This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.


# ----------- PSEUDOCODE -------------

#

# -------------- CODE ----------------
from math import sqrt


def is_triangle(num: int) -> bool:
    result = (sqrt(1 + 8*num) - 1)/2

    if result % int(result) == 0:
        return True
    else:
        return False


def is_square(num: int) -> bool:
    result = sqrt(num)

    if result % int(result) == 0:
        return True
    else:
        return False


def is_pentagonal(num: int) -> bool:
    result = (sqrt(1 + 24*num) + 1)/6

    if result % int(result) == 0:
        return True
    else:
        return False


def is_hexagonal(num: int) -> bool:
    result = (sqrt((8*num) + 1) + 1)/4

    if result - int(result) == 0:
        return True
    else:
        return False


def is_heptagonal(num: int) -> bool:
    result = (3 + sqrt(9 + 40*num))/10

    if result % int(result) == 0:
        return True
    else:
        return False


def is_octogonal(num: int) -> bool:
    result = (sqrt(1 + 3*num) + 1)/3

    if result % int(result) == 0:
        return True
    else:
        return False


def combine_num(half_1: int, half_2: int) -> int:
    str_1 = str(half_1)
    str_2 = str(half_2)
    str_connected = str_1 + str_2
    result_int = int(str_connected)

    return result_int


def is_cyclical(num: int, calculate=[True, True, True, True, True]) -> list:
    result = []

    is_tri = is_triangle(num)
    is_sq = is_square(num)
    is_pen = is_pentagonal(num)
    is_hex = is_hexagonal(num)
    is_hept = is_heptagonal(num)
    is_octo = is_octogonal(num)

    wip = [is_tri, is_sq, is_pen, is_hex, is_hept, is_octo]

    for i in range(0, 6):
        result.append(wip[i])

    return result


def compare_bool_list(list1: list, list2: list) -> list:
    result = list1.copy()
    for i in range(0, 5):
        if list2[i]:
            result[i] = False
    return result


def is_list_cyclical(c_list: list) -> bool:
    result = [0, 0, 0, 0, 0, 0]

    for num in c_list:
        is_tri = is_triangle(num)
        is_sq = is_square(num)
        is_pen = is_pentagonal(num)
        is_hex = is_hexagonal(num)
        is_hept = is_heptagonal(num)
        is_octo = is_octogonal(num)

        wip = [is_tri, is_sq, is_pen, is_hex, is_hept, is_octo]

        for answ in wip:
            if answ == True:
                index = wip.index(answ)
                result[index] += 1

    if result[3] != 0:
        print(result)
    for i in result:
        if i == 0:
            return False
    return True

    result = []
    for h1 in range(10, 100):

        for h2 in range(10, 100):
            num_1 = combine_num(h1, h2)
            is_cycl = is_cyclical(num_1)

            if True in is_cycl and h2 != h1:

                for h3 in range(10, 100):
                    num_2 = combine_num(h2, h3)
                    is_cycl2 = is_cyclical(num_2)

                    if True in is_cycl2 and h3 not in [h1, h2]:

                        for h4 in range(10, 100):
                            num_3 = combine_num(h3, h4)
                            is_cycl3 = is_cyclical(num_3)

                            if True in is_cycl3 and h4 not in [h1, h2, h3]:

                                for h5 in range(10, 100):
                                    num_4 = combine_num(h4, h5)
                                    is_cycl4 = is_cyclical(num_4)

                                    if True in is_cycl4 and h5 not in [h1, h2, h3, h4]:

                                        for h6 in range(10, 100):
                                            num_5 = combine_num(h5, h6)
                                            is_cycl5 = is_cyclical(
                                                num_5)

                                            if True in is_cycl5 and h6 not in [h1, h2, h3, h4, h5]:

                                                num_6 = combine_num(h6, h1)
                                                is_cycl6 = is_cyclical(
                                                    num_6)

                                                if True in is_cycl6:

                                                    result = [num_1, num_2, num_3,
                                                              num_4, num_5, num_6]

                                                    is_list_cyc = is_list_cyclical(
                                                        result)

                                                    if is_list_cyc:
                                                        print(
                                                            result, sum(result))
                                                        print('')


def triangle_gen(start: int, stop: int) -> int:
    num = 1
    result = 0
    while result <= stop:
        result = (num * (num + 1)) // 2
        if stop >= result >= start:
            yield result
        num += 1


def square_gen(start: int, stop: int) -> int:
    num = 1
    result = 0
    while result <= stop:
        result = num * num
        if stop >= result >= start:
            yield result
        num += 1


def pentagonal_gen(start: int, stop: int) -> int:
    num = 1
    result = 0
    while result <= stop:
        result = (num * (3 * num - 1)) // 2
        if stop >= result >= start:
            yield result
        num += 1


def hexagonal_gen(start: int, stop: int) -> int:
    num = 1
    result = 0
    while result <= stop:
        result = num * (2 * num + 1)
        if stop >= result >= start:
            yield result
        num += 1


def heptagonal_gen(start: int, stop: int) -> int:
    num = 1
    result = 0
    while result <= stop:
        result = (num * (5 * num - 3)) // 2
        if stop >= result >= start:
            yield result
        num += 1


def octagonal_gen(start: int, stop: int) -> int:
    num = 1
    result = 0
    while result <= stop:
        result = num * (3 * num - 2)
        if stop >= result >= start:
            yield result
        num += 1


def is_next(num1: int, num2: int) -> bool:
    num1_endstr = str(num1)[-2:]
    num2_startstr = str(num2)[:2]

    return num1_endstr == num2_startstr


def main():
    start = 1000
    end = 9999

    tri_list = [i for i in triangle_gen(start, end)]
    squ_list = [i for i in square_gen(start, end)]
    pen_list = [i for i in pentagonal_gen(start, end)]
    hex_list = [i for i in hexagonal_gen(start, end)]
    hep_list = [i for i in heptagonal_gen(start, end)]
    octo_list = [i for i in octagonal_gen(start, end)]

    all_list = {
        3: [n for n in tri_list],
        4: [n for n in squ_list],
        5: [n for n in pen_list],
        6: [n for n in hex_list],
        7: [n for n in hep_list],
        8: [n for n in octo_list]
    }

    nums = []
    all_list_help = all_list.copy()
    for k in all_list:
        for n in all_list[k]:

            all_list_2 = all_list.copy()
            all_list_2.pop(k)
            for k2 in all_list_2:
                for n2 in all_list[k2]:

                    if is_next(n, n2):

                        all_list_3 = all_list_2.copy()
                        all_list_3.pop(k2)
                        for k3 in all_list_3:
                            for n3 in all_list[k3]:

                                if is_next(n2, n3):

                                    all_list_4 = all_list_3.copy()
                                    all_list_4.pop(k3)
                                    for k4 in all_list_4:
                                        for n4 in all_list[k4]:

                                            if is_next(n3, n4):

                                                all_list_5 = all_list_4.copy()
                                                all_list_5.pop(k4)
                                                for k5 in all_list_5:
                                                    for n5 in all_list[k5]:

                                                        if is_next(n4, n5):

                                                            all_list_6 = all_list_5.copy()
                                                            all_list_6.pop(k5)
                                                            for k6 in all_list_6:
                                                                for n6 in all_list[k6]:

                                                                    if is_next(n5, n6) and is_next(n6, n):
                                                                        print(
                                                                            n, n2, n3, n4, n5, n6)
                                                                        print(
                                                                            k, k2, k3, k4, k5, k6)
                                                                        print(
                                                                            'sum =', n+n2+n3+n4+n5+n6)
                                                                        return

# -------------- TESTS ---------------


def test_is_triangle():
    # given
    num = 15
    # when
    result = is_triangle(num)
    # then
    assert result == True
    assert type(result) == bool
    assert is_triangle(10) == True
    assert is_triangle(12) == False


def test_is_square():
    # given
    num = 4
    # when
    result = is_square(num)
    # then
    assert result == True
    assert type(result) == bool
    assert is_square(81) == True
    assert is_square(60) == False


def test_is_pentagonal():
    # given
    num = 92
    # when
    result = is_pentagonal(num)
    # then
    assert result == True
    assert type(result) == bool
    assert is_pentagonal(117) == True
    assert is_pentagonal(48) == False
    assert is_pentagonal(92) == True


def test_is_hexagonal():
    # given
    num = 45
    # when
    result = is_hexagonal(num)
    # then
    assert result == True
    assert type(result) == bool
    assert is_hexagonal(15) == True
    assert is_hexagonal(16) == False
    assert is_hexagonal(946) == True


def test_is_heptagonal():
    # given
    num = 55
    # when
    result = is_heptagonal(num)
    # then
    assert result == True
    assert type(result) == bool
    assert is_heptagonal(34) == True
    assert is_heptagonal(35) == False


def test_is_octogonal():
    # given
    num = 8
    # when
    result = is_octogonal(num)
    # then
    assert result == True
    assert type(result) == bool
    assert is_octogonal(65) == True
    assert is_octogonal(66) == False


def test_combine_num():
    half1 = 23
    half2 = 87
    assert combine_num(half1, half2) == 2387


# --------------- RUN ---------------
if __name__ == '__main__':
    main()


# ------------ RESULT -------------

# 8128 2882 8256 5625 2512 1281
# 3 5 6 4 7 8
# sum = 28684
