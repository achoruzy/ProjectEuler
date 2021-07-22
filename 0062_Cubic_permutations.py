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
    '''Checks for number of permutations along list
    
    params:
        cubes: list -> list of cubes of equal lenght
        permuts: int -> how many permutations to be found

    returns:
        list of found permutations if len(result) == permuts
        empty list if else
    '''
    result = []

    for i in cubes:
        result_iter = []
        i_str = str(i)

        cubes_iter = cubes
        cubes_iter.remove(i)
        for j in cubes_iter:
            j_str = str(j)
            if sorted(i_str) == sorted(j_str):
                if len(result_iter) == 0:
                    result_iter.append(i)
                result_iter.append(j)
        
        if len(result_iter) == permuts:
            result.append(result_iter)

    for i in result:
        if len(i) == permuts:
            return i
    return []


def main():
    iter = 3
    while True:
        cubes = cube_generator(iter)
        permuts = 5
        list_permuts = compare_for_permutations(cubes, permuts)
        
        if len(list_permuts) == permuts:
            return list_permuts

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


def test_compare_for_permutations():
    test_list_1 = [125, 216, 343, 512, 729]
    test_param_1 = 5
    assert compare_for_permutations(test_list_1, test_param_1) == []

    test_list_2 = [8766, 1234, 2341, 3421, 2431, 9090]
    test_param_2 = 4
    assert compare_for_permutations(test_list_1, test_param_2) == [1234, 2341, 3421, 2431]

# --------------- RUN ---------------
if __name__ == '__main__':
    result_list = main()
    print(result_list)
    print(min(result_list))
    print(result_list[0]**(1./3))


# ------------ RESULT -------------
# 140283769536