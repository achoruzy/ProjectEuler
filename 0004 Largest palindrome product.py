# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
my_list = []
num = 0
for a in range(100, 999):
    for b in range(100, 999):
        num = a * b
        if str(num) == str(num)[::-1]:
            my_list.append(num)

print(max(my_list))
