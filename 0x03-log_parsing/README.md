# Minimum Operations

> This project was mock interview preparation.

## Summary

I revisited Python concepts like: Prime Factorization, Greedy Algorithms, etc.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-minoperations.py](https://github.com/Ebube-Ochemba/alx-interview/blob/main/0x00-pascal_triangle/0-minoperations.py): In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.
  - Prototype: `def minOperations(n)`
  - Returns an integer
  - If `n` is impossible to achieve, return `0`

Example:

`n = 9`
`H` => `Copy All` => `Paste` => `HH` => `Paste` => `HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`

> [0-main.py](./0-main.py): A test case for the program. Provided by Alx.
