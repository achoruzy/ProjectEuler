# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
# ------------------

from string import ascii_uppercase

# File read and get into usage
with open('0023names.txt', mode='r') as file:
    names = file.read()
    names_list = sorted(names.replace('"', '').split(','))


# Letter counting dict
letter_worth = {k: ascii_uppercase.index(k)+1 for k in ascii_uppercase}

# name worth count func


def name_worth(name):
    score = 0
    for i in name:
        score += letter_worth.get(i)
    return score


# name index func
def name_index(i, listing):
    return listing.index(i)+1


# name score func
def name_score(i, listing):
    return name_index(i, listing) * name_worth(i)


# total score for file
def total_score(file_as_list):
    score = 0
    for i in file_as_list:
        score += name_score(i, file_as_list)
    file_as_list.remove(i)
    return score


# CHECK
# print(name_worth('COLIN'))
# print(name_score('COLIN', names_list))

# RESULT
print(total_score(names_list))
