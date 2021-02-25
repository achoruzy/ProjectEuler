# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
prime_num_list = []

while num != 1:
    for i in range(2, num):
        if num % i == 0:
            prime_num_list.append(i)
            num = int(num / i)
            print(i, num)
