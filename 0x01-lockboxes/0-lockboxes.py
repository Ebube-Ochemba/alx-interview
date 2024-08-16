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

    for target_box in range(1, len(boxes) - 1):
        can_be_unlocked = False
        for box_with_key in range(len(boxes)):
            can_be_unlocked = (
                target_box in boxes[box_with_key] and
                target_box != box_with_key
            )
            if can_be_unlocked:
                break
        if can_be_unlocked is False:
            return can_be_unlocked

    return True
