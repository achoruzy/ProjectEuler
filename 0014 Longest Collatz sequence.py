# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence(starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet(Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# Note: Once the chain starts the terms are allowed to go above one million.

def s_odd(n):
    return 3 * n + 1


def s_even(n):
    return n/2


starting_num = 2
longest_chain = 0
highest_num = 0

while starting_num <= 1000000:

    seq_num = starting_num
    chain = 0
    while seq_num > 1:
        if seq_num % 2 == 0:
            seq_num = s_even(seq_num)
            chain += 1
        else:
            seq_num = s_odd(seq_num)
            chain += 1

    if chain > longest_chain:
        longest_chain = chain
        highest_num = starting_num

    starting_num += 1

print(longest_chain)
print(highest_num)
