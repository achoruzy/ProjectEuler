# PROBLEM 59 XOR decryption

# Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

# Bitwise operators are used to compare(binary) numbers:
# Operator 	Name 	Description
# &  	AND 	Sets each bit to 1 if both bits are 1
# | 	OR 	    Sets each bit to 1 if one of two bits is 1
# ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
# ~  	NOT 	Inverts all the bits
# << Zero fill left shift  Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> Signed right shift  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# chr(107) - character from ascii code
# ord(i) - ascii code from character

# ----------- PSEUDOCODE -------------

# FIND DECRYPTION KEY:
# open file
# separate data to a list of integers
# xor each with keygen
# check if there is any next characters for and word in the list

# -------------- CODE ----------------
from string import ascii_lowercase


def xor(x, y):
    """ (x OR y) AND (NOT x OR NOT y)"""
    return ((x | y) & (~x | ~y))


def encryption_keygen():
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                yield a+b+c


def generate_rotable():
    pass


def list_str_to_int(char_list) -> list:
    result = []
    for i in char_list:
        i_int = int(i)
        result.append(i_int)

    return result


def decrypt_word(word: str) -> list:
    pass


def check_common_word(decrypted_list: list, common_word: str) -> bool:
    word_list = []
    for i in common_word:
        i_ascii = ord(i)
        word_list.append(i_ascii)

    list_len = len(decrypted_list)
    word_len = len(word_list)

    for i in range(0, list_len-word_len+1):
        check_list = decrypted_list[i:i+word_len]
        if word_list == check_list:
            return True

    return False


def open_cipher(path: str) -> list:
    ascii_list = []
    with open(path, 'r') as file:
        file_str = file.read()
        char_list = file_str.split(',')
        ascii_list = list_str_to_int(char_list)
    return ascii_list

# -------------- TESTS ---------------


def test_xor():
    x = 107
    y = 42
    assert xor(x, y) == 65


def test_encryption_keygen():
    gen = encryption_keygen()
    assert next(gen) == 'aaa'
    assert next(gen) == 'aab'


def test_list_str_to_int():
    mylist = ['11', '14']
    result = list_str_to_int(mylist)
    assert result == [11, 14]


def test_check_common_word():
    word = 'and'
    decrypted_list = [101, 97, 110, 100, 123]
    result = check_common_word(decrypted_list, word)
    assert result == True


# --------------- RUN ---------------
if __name__ == '__main__':
    cipher_list = open_cipher('0059cipher.txt')
    print(cipher_list)


# ------------ RESULT -------------
