#!/usr/bin/python3
"""
    interview prepreation
"""


def minOperations(n):
    """
        this function th solve minimum operation problem using
        prime factors
    """
    step = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            step += factor
            n //= factor
        factor += 1
    return step
