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
    A_set = set(A)  # {n for n in A if n > 0}

    for i in range(1, len(A_set)):
        if i not in A_set:
            return i


@timing
def solution(A: list) -> int:
    max_A = max(A)

    if max_A <= 0:
        return 1

    return find(A)


@timing
def solution_3(A):

    max_elem = max(A)
    if max_elem <= 0:
        return 1
    else:
        return min(set(range(1, max_elem+2)) - set(A))


# --------------- RUN ---------------
if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2, 10, 11, 34, 2, 5, 6,
         7, 8, 9, 22, 12, 13, 14, 15, 16, 17, 18]
    B = [-1, -3]
    C = [876456, 267834]
    D = [i for i in range(1, 10000)]
    D.remove(9997)
    E = [i for i in range(-1000, 1000000)]
    E.remove(999997)
    print(solution(A))
    print(solution(B))
    print(solution(C))
    print(solution(D))
    print(solution(E))
    print(solution_3(E))

# ------------ RESULT -------------
