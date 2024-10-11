#!/usr/bin/python3
"""Module for the canUnlockAll function"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    :param boxes: A list of lists where each inner list represents the keys in a box
    :return: True if all boxes can be opened, else False
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key not in unlocked and new_key < n:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
