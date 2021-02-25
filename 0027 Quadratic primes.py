# Euler discovered the remarkable quadratic formula:

# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n

# Find the product of the coefficients,
# and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with.

from math import sqrt


def delta(b: int, c: int):
    delta = (2*b) - (4*1*c)
    return delta


def quadratics(b: int, c: int):
    delt = delta(b, c)
    if delt > 0:
        n1 = ((-1*b)-(sqrt(delta)))/2
        n2 = ((-1*b)+(sqrt(delta)))/2
        return [n1, n2]
    elif delt == 0:
        n0 = (-1*b)/2
        return n0
    else:
        return None


def intCheck(num):
    '''
    Checks if number is integer type
    '''
    if num == 0:
        return True
    elif num % (int(num)) == 0:
        return True
    else:
        return False


def ifPrimes(quadratics):
    '''
    Returns True if quadratics are prime numbers
    '''
    quadratics = abs(quadratics)
    if type(quadratics) == list:
        for n in quadratics:
            if intCheck(n) == False:
                return False
            else:
                if primeCheck(n) == False:
                    return False
                else:
                    return True

    elif quadratics is None:
        return False

    else:
        if intCheck(quadratics) == True:
            if primeCheck(quadratics) == False:
                return False
            else:
                return True
        else:
            return False


def nresult(b: int, c: int, n: int):
    # n^2 + an + b = 0
    result = n*n + b*n + c
    return result


def primeCheck(num: int):
    '''
    Checks if number is a prime number
    '''
    num = int(abs(num))
    if num in [0, 1]:
        return False
    elif num % 2 == 0 and num not in [2]:
        return False
    elif num in [2, 3]:
        return True
    else:
        for div in range(3, (int(sqrt(num)) + 1)):
            if num % div == 0:
                return False
        return True


def primesChain(b: int, c: int):
    chain = 0

    while True:
        n_result = nresult(b, c, chain)
        num_plus = primeCheck(n_result)

        if num_plus == True:
            chain += 1
        else:
            break

    return chain


def loopOver(b_range: int, c_range: int):
    max_chain = {'max chain': 0,
                 'b': 0,
                 'c': 0}

    for b in range(-1*(b_range-1), b_range):
        for c in range(-1*c_range, c_range+1):

            chain = primesChain(b, c)

            if chain > max_chain['max chain']:
                max_chain['max chain'] = chain
                max_chain['b'] = b
                max_chain['c'] = c
            else:
                continue
    return max_chain


if __name__ == '__main__':
    x, y = 1000, 1000
    chain = loopOver(x, y)
    print(chain)
    print('product = ', (chain['b']*chain['c']))
