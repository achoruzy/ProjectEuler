# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTe: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

from time import time
import re

numbers = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def numTexted(num):
    ''' Function translates integer number into text. '''
    # 1 to 19
    if num < 20:
        return numbers[num]
    # 20 to 9999
    else:
        thousands = num // 1000
        thou_text = ''
        hundreds = (num // 100) - 10*thousands  # int(str(num)[-3])
        hund_text = ''
        and_text = ''
        tens = int(str(num)[-2])  # (num // 10) - 100*thousands - 10*hundreds
        tens_text = ''
        dash_text = ''
        ones = int(str(num)[-2::])
        ones_first = int(str(num)[-1])
        ones_text = ''
        if thousands != 0:
            thou_text = numbers[thousands] + ' thousand'
        if hundreds != 0:
            hund_text = ' ' + numbers[hundreds] + ' hundred'
        if (thousands != 0 or hundreds != 0) and (tens != 0 or ones != 0):
            and_text = ' and '
        if tens > 1:
            tens_text = numbers[tens*10]
        if tens > 1 and ones_first != 0:
            dash_text = '-'
        if ones < 20 and ones > 0:  # 1 to 19
            ones_text = numbers[ones]
        elif ones_first != 0:
            ones_text = numbers[ones_first]

        return thou_text + hund_text + and_text + tens_text + dash_text + ones_text


def numTextCount(num):
    ''' Function counts letters for text translated from integer number. '''
    word_list = re.findall(r'\w+', numTexted(num))
    letter_counter = 0
    for i in range(0, len(word_list)):
        letter_counter += len(word_list[i])
    return letter_counter


# Rozwiązanie:
letters_counted = 0
range_start = 1
range_end = 1000 + 1

for i in range(range_start, range_end):
    letters_counted += numTextCount(i)


print(f'There is {letters_counted} letters for translated to text numbers between {range_start} and {range_end - 1}.')

# Około 1h pracy
