# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


def nineLenList(num: int):
    axb = num
    result = []

    for a in range(2, round(axb/2)+1):
        if axb % a == 0:
            b = axb // a
            digs_abaxb = str(a) + str(b) + str(axb)

            if len(digs_abaxb) == 9:
                result.append(digs_abaxb)

    return result


def isPandigital(digits: str):
    for dig in range(1, 10):
        dig_str = str(dig)
        if digits.count(dig_str) != 1:
            return False
    return True


def hasDoublesOrZero(num: str):
    num_str = str(num)
    if '0' in num_str:
        return True

    for i in num_str:
        if num_str.count(i) > 1:
            return True
        else:
            return False


if __name__ == '__main__':
    result = []

    num = 10

    while num <= 20000:
        num += 1

        if hasDoublesOrZero(num):
            continue

        for i in nineLenList(num):
            if isPandigital(i):
                result.append(num)
                break

    print(result)
    print(len(result))
    print(sum(result))
