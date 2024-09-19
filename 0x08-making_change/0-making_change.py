#!/usr/bin/python3
""" A function that calculates coin change """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    args:
        coins : A list of coin denominations (integers greater than 0).
        total : The total amount to achieve using the given coins.

    Returns:
        The fewest number of coins required to meet the total.
            -1, if the total cannot be met
            0, if total <= 0.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        count += total // coin
        total = total % coin
        if total == 0:
            return count

    return -1


"""
Illustration by Lines
------------
19-20: If the total is 0 or less, no coins are needed

22: Sort the coins in descending order, to sort from largest to smallest

24: Track total number of coins used

26: Iterate through each coin denomination
    27: Use as many of the current coin as possible
    28: Update the total to the remainder after using the current coin
    29-30: If total is now 0, we've found exact amount, return count

32: If total isn't 0 after iterating through the coins, return -1
    This means it's impossible to meet the total with the given coins
"""
