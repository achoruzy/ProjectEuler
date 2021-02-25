# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
# ---------------

# return a list of divisors for a num


def divisors(num):
    divisors = []
    for i in range(1, round(num/2)+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def amicableCheck(num):
    num_divs = divisors(num)
    sum_divs = sum(num_divs)
    check_num_divs = divisors(sum_divs)
    sum_check_num = sum(check_num_divs)
    if num == sum_divs:
        return False
    else:
        return num == sum_check_num


def amicableNumbers(num):
    amicable_num_list = []
    for i in range(2, num):
        if amicableCheck(i):
            amicable_num_list.append(i)
    return amicable_num_list


result = amicableNumbers(10000)

print(result)
print('Sum of amicable numbers: ', sum(result))
