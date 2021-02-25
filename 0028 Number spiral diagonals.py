# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def diagonals(edge: int):

    row = 1
    last_row = 0
    total = 1
    halfrows = int((edge - 1) / 2)

    while row <= halfrows:
        a = row + last_row
        b = a + 4

        for i in range(a, b):
            c = (i * row * 2) + 1
            total += c
        last_row = row
        row += 1
    return total


print(diagonals(1001))
