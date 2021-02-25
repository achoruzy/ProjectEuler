# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# ---------------

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_list = [0, 1, 2, 3]
result_permutation = []


def listProduct(li: list):
    '''
    Calculates how many permutations are available for the list.
    '''
    product = 1
    count = 1
    for i in li:
        product *= count
        count += 1
    return product


def seekedPermutation(seeked_location: int, num_list: list):
    '''
    Returns permutation of a list <num_list> arguments from desired position <seeked_location>.
    '''
    # Help list for removing next items 'num_to_go' from argument list:
    help_list = num_list

    if len(help_list) > 1:
        while listProduct(help_list) > 1:

            current_product = listProduct(help_list)
            perm_for_num = int(current_product / len(help_list))
            num_to_go = 0
            # Loop to find in which group for which item from list the seeked position is
            for i in range(0, len(help_list)):
                # If seeked position is between then 'num_to_go' is found
                if ((i*perm_for_num)+1) <= seeked_location <= ((i+1)*perm_for_num):
                    num_to_go = help_list[i]
                    help_list.remove(num_to_go)
                    seeked_location -= i*perm_for_num
                    break
            # Appending next position to return list:
            result_permutation.append(num_to_go)
            # Calling recursion for the function:
            seekedPermutation(seeked_location, help_list)

    # Append last item:
    else:
        result_permutation.append(help_list[0])

    return result_permutation


print(seekedPermutation(1000000, num_list))
