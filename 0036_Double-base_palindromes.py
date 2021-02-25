# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

# -------------- CODE ------------------

def is_palindromic(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


def for_check_binary_base_2(num):
    bin_num = str(bin(num)).replace('0b', '')
    return bin_num


# -------------- TESTS ------------------


def test_is_palindromic():
    # given
    num = 585
    # when
    result = is_palindromic(num)
    # then
    assert result == True
    assert is_palindromic(1001001001) == True
    assert is_palindromic(45678) == False
    assert type(is_palindromic(87246)) == bool
    assert is_palindromic('1001') == True


def test_for_check_binary_base_2():
    # given
    num = 585
    # when
    result = for_check_binary_base_2(num)
    # then
    assert result == '1001001001'
    assert for_check_binary_base_2(2) == '10'
    assert type(for_check_binary_base_2(3456)) == str


# --------------- RUN -------------------
if __name__ == '__main__':
    result_sum = 0
    for i in range(1, 1000000):
        if is_palindromic(i) and is_palindromic(for_check_binary_base_2(i)):
            result_sum += i

    print(result_sum)
