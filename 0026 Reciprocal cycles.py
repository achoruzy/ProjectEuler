# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# -----------------------------------------------------------------------


# divising 1 by num
def divOneByNum(den):
    '''
    Function divises 1 by given number (denominator).
    '''
    # Variables
    numerator = 1
    rest = numerator % den
    counter = 0
    result_str = '0,'

    # Help coefficient
    if den < 10:
        k = 10
    elif 10 <= den < 100:
        k = 100
    else:
        k = 1000

    while rest != 0 and counter <= 10000:
        # Maths
        counter_2 = 1
        while rest < den:
            rest *= 10
            counter_2 *= 10
            if counter_2 > 10:
                result_str += str('0')

        div_res = rest // den
        result_str += str(div_res)
        rest = rest - (den * div_res)

        # Avoidance of infinity loop
        counter += 1

    return result_str


def findCycle(num_str: str):
    last_len = 0
    last_count = 0

    if len(num_str) > 6:
        if num_str[4] == num_str[5]:
            return 0
        else:
            pass
    else:
        return 0

    for i in range(2, 5):
        for j in range(i+3, len(num_str)):
            count = num_str.count(num_str[i:j])

            if count < last_count*0.7:
                return last_len

            lenght = len(num_str[i:j])
            pattern = num_str[i:j]

            if lenght > last_len and count > 1:
                last_len = lenght
                last_count = count
                # print(count, lenght, num_str[i:j])

    return last_len


# print(divOneByNum(723))
# print(findCycle(divOneByNum(723)))

def mainCheck():
    len_max = 0
    i_max = 0
    for i in range(2, 1000):
        long = findCycle(divOneByNum(i))
        # print(i, long)
        if long > len_max:
            len_max = long
            i_max = i
    return print('number: ', i_max, ', long: ', len_max)


mainCheck()
