# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


# -------------- CODE ----------------
from math import sqrt


def is_prime(num: (int, str)) -> bool:
    num = int(num)

    if num == 2:
        return True

    if num % 2 == 0 or num in (0, 1):
        return False
    elif num == 3:
        return True

    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False

    return True


def check_truncbility(num: str) -> bool:
    num_str = str(num)

    for i in ['4', '6', '8', '0']:
        if i in num_str:
            return False

    if not is_prime(num_str):
        return False

    for i in range(1, len(num_str)):
        if not is_prime(num_str[:i]):
            return False

    for i in range(1, len(num_str)):
        if not is_prime(num_str[i:]):
            return False

    return True


# -------------- TESTS ---------------
def test_is_prime():
    # given
    num_1 = 3797
    num_2 = 888
    # when
    result_1 = is_prime(num_1)
    result_2 = is_prime(num_2)
    # then
    assert result_1 == True
    assert result_2 == False
    assert type(is_prime(3456)) == bool
    assert is_prime(1) == False
    assert is_prime(3) == True
    assert is_prime(55) == False


def test_check_truncbility():
    # given
    num = 3797
    # when
    result = check_truncbility(num)
    # then
    assert result == True
    assert type(check_truncbility(5768)) == bool
    assert check_truncbility(232) == False
    assert check_truncbility(41) == False
    assert check_truncbility(3119) == False
    assert check_truncbility(3739) == False
    assert check_truncbility(23) == True


# --------------- RUN ---------------
if __name__ == '__main__':
    result_items = []
    item_counter = 1
    counter = 11

    while item_counter <= 11:
        if check_truncbility(counter):
            result_items.append(counter)
            item_counter += 1

        counter += 1

    print(result_items)
    print(sum(result_items))

# [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# 748317
