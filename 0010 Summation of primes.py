# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from time import time
import math

sum = 2
sum_range = 1999999
#time_1 = time()

for i in range(3, sum_range, 2):
    prime = True
    for j in range(3, 1 + math.floor(math.sqrt(i)), 2):  # floor zaokragla w dol
        if i % j == 0:
            prime = False
            break

    if prime == True:
        sum += i
        #print(i, sum)

#time_2 = time()


print(sum)
#print(time_2 - time_1)
