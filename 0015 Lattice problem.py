# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# Starting point

start_point = (0, 0)

# Finish point

finish_point = (20, 20)

# Can x += 1 or y += 1 at once only
# So entire number of actions has to be fpx + fpy
# Think as 2d vectors

# czyli ilość ruchów musi równać sie łącznie 40 (20+20)
# i sekwencja ruchów jest sekwencją kolejnych ruchów x i y z ograniczeniem ilości jednego znaku do 20 np.
# [x,y,y,y,x,x,y,y,x,x,x,y,y,y,x,x,y,y,x,x]
# do wykonania permutacja matematyczna z powtórzeniami dla dwóch możliwości przy zadanej ilości miejsc


def factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


def permutation(grid_h, grid_w):
    return int(factorial(grid_h + grid_w) / (factorial(grid_h) * factorial(grid_w)))


print(permutation(20, 20))
