# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


i = 2
count = 0

while count <= 10001:
    check = 0
    for d in range(2, i-1):
        if i % d == 0:
            check += 1
    if check == 0:
        count += 1
        print(i, count)
    i += 1

print(i)
