# Brodie Heywood
# November 26, 2018

"""Euclid's Method"""

import doctest


def gcd(a, b):
    """Find greatest common divisor of two integers.

    Use Euclid's method to find the largest number that can divide two given numbers without leaving a remainder.
    PARAM: a and b, integers for which the greatest common divisor will be found
    PRECONDITION: a and b must be non-zero integers
    POSTCONDITION: calculates greatest common divisor of a and b
    RETURN: greatest common divisor of parameters a and b as an integer
    >>> gcd(1, 1)
    1
    >>> gcd(45, 25)
    5
    >>> gcd(-45, -25)
    5
    >>> gcd(40, -52)
    4
    >>> gcd(-40, 52)
    4
    >>> gcd(7, 13)
    1
    """
    if a and b != 0:

        if a > b:
            greater = a
            lesser = b
        elif b > a:
            greater = b
            lesser = a
        else:  # a == b
            return a  # can also return b

        while lesser != 0:
            initial_lesser = lesser
            lesser = greater % lesser
            greater = initial_lesser

        return abs(greater)

    else:
        if a == 0:
            invalid_param = 'a'
        else:  # b == 0
            invalid_param = 'b'
        raise Exception('Parameters a and b must be non-zero integers. The value of ' + invalid_param + ' was zero.')


def main():
    the_gcd = gcd(-25, 15)
    print(the_gcd)


if __name__ == '__main__':
    main()
    doctest.testmod()
