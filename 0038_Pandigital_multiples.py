# Take the number 192 and multiply it by each of 1, 2, and 3:

#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# ------------ PSEUDOCODE ------------

# largest pandigital is 987654321 -> this is going to be digit list to start checking

# set pandigital number generator
# set it in a while loop for next pandigitals to check
# check conditions:
# it is always that the concatenated product's first n digits (call it A_num) are then A_num * 1, A_num *2 ... A_num*m
# formula is A_num = aaa, A_num*2 = bbb, A_num*3 = ccc -> aaabbbccc
# thus lenght of A_num <= A_num*2 <= A_num*3 ... AND len A_num <= 4
# AND if any A_num digit in A_num*n -> False
# so check is using for loop for int(str(pandigital[0:(n <= 4)]))
# first number fulfilling conditions is the result
# return largest pandigital for condition

# -------------- CODE ----------------
from math import factorial


def pandigital(position: int) -> int:
    """ Function returns integer number from given position from combinations of 9 to 1 digits. """
    digit_list = [n for n in range(9, 0, -1)]
    help_list = digit_list.copy()
    result_list = []
    result_str = ''
    num_of_solutions = factorial(len(digit_list))
    while len(help_list) > 0:
        range_size = num_of_solutions // len(help_list)
        list_dig_within = (position-1) // range_size
        num_of_solutions //= len(help_list)
        position -= (list_dig_within * range_size)
        result_list.append(help_list.pop(list_dig_within))

    for i in result_list:
        result_str += str(i)

    return int(result_str)


def check_conditions(num) -> bool:
    """ Function checks if problem conditions are fullfilled for the pandigital number given.
    Condition: For A = int(str(num)[0:i] if str(A*1)+str(A*2)+...+str(A*n) == str(num) -> True"""
    num_str = str(num)

    for seq in range(1, (len(num_str)//2)):
        check_num = int(num_str[0:seq+1])
        multip = 1
        check_num_str = str(check_num)
        while True:
            multip += 1
            next_num = check_num * multip
            if str(next_num) not in num_str:
                break
            check_num_str += str(next_num)
            if len(check_num_str) > len(num_str):
                break
            if check_num_str == num_str:
                return True
        continue
    return False


# -------------- TESTS ---------------


def test_pandigital():
    # given
    pos = 1
    # when
    result = pandigital(1)
    # then
    assert result == 987654321
    assert pandigital(362880) == 123456789
    assert type(pandigital(7643)) == int


def test_check_conditions():
    # given
    num = 192384576
    # when
    result = check_conditions(num)
    # then
    assert result == True
    assert check_conditions(123456789) == False
    assert type(check_conditions(214365879)) == bool


# --------------- RUN ---------------
if __name__ == '__main__':
    result_number = 0
    counter_num = 0
    while counter_num <= 362880:
        counter_num += 1
        pandigit = pandigital(counter_num)
        if check_conditions(pandigit):
            result_number = pandigit
            break
    print(result_number)

# ------------ RESULT -------------
# 932718654
