#!/usr/bin/python3


def canUnlockAll(boxes):
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
