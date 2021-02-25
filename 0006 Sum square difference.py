
sq_of_sum = 0
sum_of_sq = 0

for i in range(1, 101):
    sum_of_sq += i**2
    sq_of_sum += i

sq_of_sum = sq_of_sum**2
difference = sq_of_sum - sum_of_sq

print(difference)
