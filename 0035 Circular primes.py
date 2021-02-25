# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from math import sqrt, factorial


def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
        else:
            continue
    return True


def has_permutations(num):
    digs = [i for i in str(num)]
    combinations = factorial(len(digs))
    result_list = []

    # for each combination loop
    for comb in range(0, combinations):
        help_list = digs.copy()
        help_list_result = []

    # find combination

        while len(help_list) > 0:
            sol_per_dig = factorial(len(help_list) - 1)

            seek_pos = comb // sol_per_dig

            help_list_result.append(help_list[seek_pos])
            help_list.remove(help_list[seek_pos])

            comb -= sol_per_dig * seek_pos

        # list to str to int
        comb_str = str()

        for dig in help_list_result:
            comb_str += dig

        comb_int = int(comb_str)

        # check if prime
        if is_prime(comb_int) == False:
            return []
        else:
            result_list.append(comb_int)
            continue

    print(combinations, digs)
    return result_list


def is_circular(num):
    digs = [i for i in str(num)]
    result_list = []

    help_list = digs
    counter = 0

    while counter != len(digs):
        help_list.append(help_list.pop(0))
        curr_num_str = str()

        for i in help_list:
            curr_num_str += i

        if is_prime(int(curr_num_str)) == False:
            return []
        else:
            result_list.append(int(curr_num_str))

        counter += 1

    return result_list


# ---------------------------------------------


if __name__ == '__main__':
    circular_prime_list = [2]

    for i in range(3, 1000000, 2):
        if is_prime(i) == False and i in circular_prime_list:
            continue
        elif i in circular_prime_list:
            continue
        else:
            add_list = is_circular(i)
            for i in add_list:
                if i in circular_prime_list:
                    pass
                else:
                    circular_prime_list.append(i)

    print(sorted(circular_prime_list))
    print(len(circular_prime_list))

# [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]
# 55
