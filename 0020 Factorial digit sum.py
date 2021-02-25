# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# Silnia


def factorial(num):
    fac = 1
    while num >= 1:
        fac *= num
        num -= 1
    return fac


def sumOfSigns(num):
    sumofsigns = 0
    for i in str(num):
        sumofsigns += int(i)
    return sumofsigns


print(sumOfSigns(factorial(100)))
