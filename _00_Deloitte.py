# Write a function:def solution(A)that, given an array A of N integers, returns the smallest positiveinteger (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an eficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


# ----------- PSEUDOCODE -------------

#

# -------------- CODE ----------------
from time import time


def timing(func):
    """ Decorator function for calculating working time of another function."""
    def wrapper(*args, **kwargs):
        time_1 = time()
        return_var = func(*args, **kwargs)
        time_2 = time()
        print('Function worked: ', str(time_2-time_1)[:5], ' sec.')
        return return_var
    return wrapper


def find(A: list) -> int:
    A_set = {n for n in A if n > 0}

    for i in range(1, len(A)):
        if i not in A_set:
            return i


@timing
def solution(A: list) -> int:
    max_A = max(A)

    if max_A <= 0:
        return 1

    return find(A)


# --------------- RUN ---------------
if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    B = [-1, -3]
    print(solution(A))
    print(solution(B))


# ------------ RESULT -------------