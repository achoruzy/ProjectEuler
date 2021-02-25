# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44

# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# -------------------------

num_list = []


def fifthPowers():
    dictionary = {k: k**5 for k in range(0, 10)}
    counter = 32
    while counter < 1000000:
        sum_digs = 0
        for i in str(counter):
            i_int = int(i)
            sum_digs += dictionary.get(i_int)
        if counter == sum_digs:
            num_list.append(counter)
        else:
            pass
        counter += 1
    return num_list


print(fifthPowers())
print(sum(num_list))
