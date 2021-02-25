# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


def frac_check(a, b, x):
    num = int(str(a) + str(x))
    den = int(str(x) + str(b))

    if num / den >= 1:
        return False
    elif num / den == a / b:
        return True
    else:
        return False


def canc_frac():
    count = 0
    frac_list = []

    for x in range(1, 10):
        for a in range(1, 10):
            for b in range(1, 10):
                if frac_check(a, b, x) == True:
                    numerator = str(a) + str(x)
                    denumerator = str(x) + str(b)

                    fraction = numerator + '/' + denumerator

                    frac_list.append([int(numerator), int(denumerator)])
                    count += 1
    return frac_list


def lowest_common(list_obj):
    help_list = []
    result = []

    for i in list_obj:
        for j in range(i[0], 1, -1):
            if i[0] % j == 0 and i[1] % j == 0:
                a = i[0] / j
                b = i[1] / j
                help_list.append([int(a), int(b)])
                break

    return help_list


def shared_denominator_sum(num_list):
    num = []
    den = 1

    for i in num_list:
        den *= i[1]

        n = i[0]
        for j in range(0, len(num_list)):
            n *= num_list[j][1]
        n /= i[1]
        num.append(int(n))

    numerator = sum(num)

    return [[numerator, den]]


def shared_denominator_prod(num_list):
    num = 1
    den = 1

    for i in num_list:
        num *= i[0]
        den *= i[1]

    return [[num, den]]


if __name__ == '__main__':

    my_list = canc_frac()
    print(my_list)
    shorted_list = lowest_common(my_list)
    print(shorted_list)

    fraction_to_short = shared_denominator_prod(shorted_list)
    print(fraction_to_short)
    shorted_fraction = lowest_common(fraction_to_short)
    print(shorted_fraction)
