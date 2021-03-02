# PROBLEM 41 Coded triangle numbers

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

# ----------- PSEUDOCODE -------------

# open the document
# read the document in a way that can use words separately
# for each word
#   calculate sum of letter values
#   check if the sum is triangle number - if is
#       add +1 to result counter

# -------------- CODE ----------------

# Generator
def char_range(letter_start: str, letter_end: str):
    """Generates characters from start to end"""
    for letter in range(ord(letter_start), ord(letter_end)+1):
        yield chr(letter)


def word_pts_count(word: str) -> bool:
    letter_pts = {k: v for k, v in zip(char_range('A', 'Z'), range(1, 27))}
    summed = 0
    for i in word:
        summed += letter_pts[i]
    return summed


def is_triangle_word(pts: int) -> bool:
    for i in range(1000):
        if 2*pts == i**2 + i:
            return True
    return False


# -------------- TESTS ---------------


def test_word_pts_count():
    # given
    word = 'SKY'
    # when
    result = word_pts_count(word)
    # then
    assert result == 55


def test_is_triangle_word():
    # given
    word = 55
    # when
    result = is_triangle_word(word)
    # then
    assert result == True


# --------------- RUN ---------------
if __name__ == '__main__':
    result = 0
    # File read and get into usage
    with open('0042words.txt', mode='r') as file:
        words = file.read()
        # words_list = sorted(names.replace('"', '').split(','))
        for word in sorted(words.replace('"', '').split(',')):
            pts = word_pts_count(word)
            if is_triangle_word(pts):
                result += 1
    print(result)


# ------------ RESULT -------------

# 162
