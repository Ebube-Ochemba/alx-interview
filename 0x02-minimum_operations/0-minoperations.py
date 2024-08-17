#!/usr/bin/python3
"""Minimum Operations"""


def calcPrimeFactors(number):
    """Calculates the prime factors of a given number.

    return: A list of the prime factors of the input number.
    """
    div = 2
    primes = []
    rem_num = number

    while (div <= rem_num / 2):  # Any num > (num / 2) can't be a factor
        if rem_num % div == 0:
            primes.append(div)
            rem_num //= div  # reduce number
        else:
            div += 1

    if rem_num > 1:  # remaining factor greater > 1 must be prime
        primes.append(int(rem_num))

    return primes


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    if n <= 1:
        return 0

    # Get the prime factors of n
    factors = calcPrimeFactors(n)

    # The minimum operations are the sum of the prime factors
    return sum(factors)
