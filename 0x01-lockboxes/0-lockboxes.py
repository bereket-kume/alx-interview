#!/usr/bin/python3
"""
    solution for lockboxe
"""


def canUnlockAll(boxes):
    """
        this function solve lock box using
        bfs S
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = list(boxes[0])

    while keys:
        current_key = keys.pop()
        if current_key < n and not unlocked[current_key]:
            unlocked[current_key] = True
            for key in boxes[current_key]:
                if key < n and not unlocked[key]:
                    keys.append(key)

    return all(unlocked)
