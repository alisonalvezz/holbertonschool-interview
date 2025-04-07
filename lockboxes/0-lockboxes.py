#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    Attributes:
    boxes: A list of lists where each inner list represents a box
    and contains keys to other boxes
    Returns:
    a bool thats true if all boxes can be unlocked, false otherwise
    """
    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if 0 <= key < n and key not in opened:
                    stack.append(key)

    return len(opened) == n
