# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

two_pounds = 200    # n
pennies = [200, 100, 50, 20, 10, 5, 2, 1]  # m

'''
Simplest solution:
func(n,m)

if n = 0 then func() = 1
if m = 0 then func() = 0
if n < 0 then func() = 0

thus:
func(n, m) = func(n, m-1) + func(n-m, m)
'''


def partitions(n=200, m=0, list=pennies):
    if n == 0:
        return 1
    elif m == len(list) or n < 0:
        return 0
    else:
        return partitions(n - list[m], m) + partitions(n, m + 1)


print(partitions())
