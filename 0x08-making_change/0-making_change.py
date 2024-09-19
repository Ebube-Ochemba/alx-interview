#!/usr/bin/python3
""" A function that calculates coin change """


def makeChange(coins, total):
    if total <= 0:
        return 0

    # array for coin "change" calculation
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coin needed to total 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


"""
Guide
-----
I. Lines 10 - 11
    - Initialize dp array with a large number, (total+1 is larger than any
    possible result). i.e. set all indexes to an infinite value
    - Set Base case: 0 coins needed to make 0 total

II. Lines 13 - 16
    - Iterate over every amount from 1 to total
    - Check each coin to see if it can contribute to the current amount

III. Line 18
    - If dp[total] is still inf, it means no solution was found
"""
