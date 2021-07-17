# PROBLEM 62 Cubic permutations

# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

# ----------- PSEUDOCODE -------------

# generate cubes - do it for same lenght numbers
# look for numbers having same digits - prmutations

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
    return wrapper()


def cube_generator(lenght: int) -> list:
    '''Generates lists of cubes <x^3> of specified number of digits'''
    iter = 1
    result = []
    while True:
        cube = iter ** 3
        if len(str(cube)) == lenght:
            result.append(cube)
        elif len(str(cube)) > lenght:
            break
        iter += 1

    return result


def compare_for_permutations(cubes: list, permuts: int) -> list:
    '''Checks for number of permutations along list'''
    result = []
    for i in cubes:
        i_sorted_str = str(i)
        for j in cubes.remove(i):
            j_sorted_str = str(i)
            if i_sorted_str == j_sorted_str:
                if len(result) == 0:
                    result.append(i)
                result.append(j)
    return result

def main():
    iter = 4
    while True:
        cubes = cube_generator(iter)
        print(cubes)
        if iter == 25:
            break
        iter += 1


# -------------- TESTS ---------------

def test_cube_generator():
    # given
    len = 3
    # when
    result = cube_generator(len)
    # then
    assert result == [125, 216, 343, 512, 729]


# --------------- RUN ---------------
if __name__ == '__main__':
    main()


# ------------ RESULT -------------
