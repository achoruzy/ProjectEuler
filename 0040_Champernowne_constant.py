# PROBLEM 40 Champernowne's constant

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# ----------- PSEUDOCODE -------------
# <on papernotes>


# -------------- CODE ----------------


def find_brute() -> list:
    result = [1]
    counter = 9
    to_find = [10, 100, 1000, 10000, 100000, 1000000]
    before_num = 1
    while counter <= 1000000:
        for dig in range(0, 10):
            num_str = str(before_num) + str(dig)
            for i in num_str:
                counter += 1
                if counter in to_find:
                    result.append(i)
                    print(i)
            before_num += 1
    return result

# -------------- TESTS ---------------


# --------------- RUN ---------------
if __name__ == '__main__':
    result_list = find_brute()
    print(result_list)

    res = 1
    for i in result_list:
        res *= int(i)
    print(res)

# ------------ RESULT -------------

# 210
