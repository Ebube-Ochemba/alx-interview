#!/usr/bin/python3
"""0-lockboxes"""


def canUnlockAll(boxes):
    """checks if all boxes can be opened
    Args:
        boxes (list): list of boxes
    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    if (type(boxes) is not list or len(boxes) == 0):
        return False

    for box_number in range(1, len(boxes) - 1):
        is_unlocked = False
        for current_box in range(len(boxes)):
            is_unlocked = (
                box_number in boxes[current_box] and
                box_number != current_box
            )
            if is_unlocked:
                break
        if is_unlocked is False:
            return is_unlocked

    return True
