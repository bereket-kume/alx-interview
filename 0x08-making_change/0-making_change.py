#!/usr/bin/python3

def makeChange(coins, total):
    """
    function to calculate change
    return amount of change
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for t in total:
        for c in coins:
            if t - c >= 0:
                dp[t] = min(dp[t], 1 + dp[t-c])
    return dp[total] if dp[total] != total + 1 else -1
