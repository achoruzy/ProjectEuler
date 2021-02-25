# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

list_curious = []

for i in range(10, 100001):
    fac_sum = 0

    for digit in str(i):
        fac_sum += factorial(int(digit))
        if fac_sum > i:
            continue

    if fac_sum == i:
        list_curious.append(i)


print(list_curious)
print(sum(list_curious))
