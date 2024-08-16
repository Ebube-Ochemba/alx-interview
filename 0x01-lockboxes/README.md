# Lockboxes

> This project was mock interview preparation.

## Summary

I revisited Python concepts like: Lists and List Comprehensions, Graph Theory Basics, Algorithmic Complexity, Recursion, Queue and Stack and Set Operations.

## Files

> Each file contains the solution to a task in the project.

- [ ] [0-lockboxes.py](https://github.com/Ebube-Ochemba/alx-interview/blob/main/0x00-pascal_triangle/0-lockboxes.py): You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.
  - Write a method that determines if all the boxes can be opened.
    - Prototype: `def canUnlockAll(boxes)`
    - `boxes` is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
      - There can be keys that do not have boxes
    - The first box `boxes[0]` is unlocked
    - Return `True` if all boxes can be opened, else return `False`

> [main_0.py](./main_0.py): A test case for the program. Provided by Alx.
