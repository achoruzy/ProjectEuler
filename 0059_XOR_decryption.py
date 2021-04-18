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

# ----------- PSEUDOCODE -------------

# FIND DECRYPTION KEY:
#

# -------------- CODE ----------------


def xor(x, y):
    """ (x OR y) AND (NOT x OR NOT y)"""
    return ((x | y) & (~x | ~y))

# -------------- TESTS ---------------


def test_xor():
    x = 107
    y = 42
    assert xor(x, y) == 65


# --------------- RUN ---------------
if __name__ == '__main__':
    print(xor(107, 'k'))


# ------------ RESULT -------------
