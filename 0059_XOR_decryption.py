# Copyright (c) 2021 Arkadiusz Choruży
# License: N/A

# ------------------------------------

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
# open file +
# separate data to a list of integers +
# xor each with keygen
# check if there is any next characters for and word in the list

# -------------- CODE ----------------
from string import ascii_lowercase


def xor(x, y):
    """ (x OR y) AND (NOT x OR NOT y)"""
    return ((x | y) & (~x | ~y))


def encryption_keygen() -> str:
    """ 3 lowercase letter key generator. """
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                yield a+b+c


def generate_rotable(keygen: str) -> str:
    """ Yields next letter from keygen in a loop."""
    while True:
        for letter in keygen:
            yield letter


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


def main_func():
    cipher_list = open_cipher('0059cipher.txt')

    for keygen in encryption_keygen():
        help_list = []
        key_sign_generator = generate_rotable(keygen)

        for sign in cipher_list:
            key_sign = next(key_sign_generator)
            decrypted_sign = xor(sign, ord(key_sign))
            help_list.append(decrypted_sign)

        if check_common_word(help_list, ' the ') and check_common_word(help_list, ' and '):
            print('\n', keygen)

            sum_ascii = 0

            for i in help_list:
                sum_ascii += i
                print(chr(i), end="")

            return print('\nSum of ascii is:', sum_ascii)

# -------------- TESTS ---------------


def test_xor():
    x = 107
    y = 42
    assert xor(x, y) == 65


def test_encryption_keygen():
    gen = encryption_keygen()
    assert next(gen) == 'aaa'
    assert next(gen) == 'aab'


def test_generate_rotable():
    text = 'abc'
    gen = generate_rotable(text)
    assert next(gen) == 'a'
    assert next(gen) == 'b'
    assert next(gen) == 'c'
    assert next(gen) == 'a'


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
    main_func()

    # ------------ RESULT -------------

# An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter
# of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of
# the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.
# Sum of ascii is: 129448
