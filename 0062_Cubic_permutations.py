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
    '''Generates lists of cubes <x^3> of specified number of digits
    
    params:
        lenght: int -> number of digits for cubes

    returns:
        list of cubes of specified number of digits
    '''
    result = []
    
    iter = 1
    while True:
        cube = iter ** 3
        cube_str_len = len(str(cube))
        if cube_str_len == lenght:
            result.append(cube)
        elif cube_str_len > lenght:
            break
        iter += 1
    
    return result


def compare_for_smallest_permutations(cubes: list, permuts: int) -> list:
    '''Checks for number of permutations along list
    
    params:
        cubes: list -> list of cubes of equal lenght
        permuts: int -> how many permutations has to be found

    returns:
        list of found permutations if len(result) == permuts
        empty list if else
    '''
    for i in cubes:
        result_for_iter = []
        i_str = str(i)

        cubes_in_iter = cubes.copy()
        cubes_in_iter.remove(i)

        for j in cubes_in_iter:
            j_str = str(j)

            if sorted(i_str) == sorted(j_str):

                if len(result_for_iter) == 0:
                    result_for_iter.append(i)
                
                result_for_iter.append(j)
        
        if len(result_for_iter) == permuts:
            # First found -> smallest
            return result_for_iter

    return []


def main(permuts: int) -> int:
    iter = 11
    while True:
        cubes = cube_generator(iter)
        list_permuts = compare_for_smallest_permutations(cubes, permuts)
        
        if len(list_permuts) == permuts:
            return list_permuts

        if iter == 13:
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


def test_compare_for_smallest_permutations():
    test_list_1 = [125, 216, 343, 512, 729]
    test_param_1 = 5
    assert compare_for_smallest_permutations(test_list_1, test_param_1) == []

    test_list_2 = [8766, 1234, 2341, 3421, 2431, 9090]
    test_param_2 = 4
    assert compare_for_smallest_permutations(test_list_2, test_param_2).sort() == [1234, 2341, 3421, 2431].sort()

# --------------- RUN ---------------
if __name__ == '__main__':
    result_list = main(5)
    print(result_list)
    print(min(result_list))
    print(round(result_list[0]**(1./3)))


# ------------ RESULT -------------
# 127035954683