#!/usr/bin/python3
"""Module to calculate minimum coins for a total."""


def make_change(coins, total):
    """
    Calculate the minimum number of coins needed to make up a total.

    Args:
        coins (List[int]): A list of coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: The minimum number of coins required to make the total,
             or -1 if it's not possible.
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    return dp[total] if dp[total] != total + 1 else -1
