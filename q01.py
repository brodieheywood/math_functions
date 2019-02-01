# Brodie Heywood
# November 26, 2018

"""Sieve of Eratosthenes"""

import doctest


def eratosthenes(upperbound: int) -> list:
    """Sieve of Eratosthenes.

    Find all prime numbers up to a given number.
    PARAM: upperbound, a positive integer; find prime numbers up to this limit
    PRECONDITION: upperbound must be a positive integer (cannot be zero)
    POSTCONDITION: calculates prime numbers below upperbound; returns empty list if upperbound is 1
    RETURN: prime numbers below upperbound as a list of integers
    >>> eratosthenes(1)
    []
    >>> eratosthenes(2)
    []
    >>> eratosthenes(3)
    [2]
    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    below_upperbound = list(range(0, upperbound))

    if upperbound > 0:
        # zero is not prime, so cross it out
        below_upperbound.remove(0)

        if upperbound > 1:
            # one is not prime, so cross it out
            below_upperbound.remove(1)

            for number in below_upperbound:
                if number < (upperbound**0.5):  # because all non-prime numbers above sqrt are multiples of non-primes below
                    for not_prime in range(number * 2, upperbound, number):
                        if not_prime in below_upperbound:
                            below_upperbound.remove(not_prime)  # more elegant than .difference, uses less memory
            return below_upperbound

        else:  # upperbound is 1
            return below_upperbound

    else:
        raise TypeError
        # raise Exception('Upperbound must be a positive integer. The value of upperbound was: {}'.format(upperbound))


def main():
    primes_below_30 = eratosthenes(30)
    print(primes_below_30)


if __name__ == '__main__':
    main()
    doctest.testmod()
