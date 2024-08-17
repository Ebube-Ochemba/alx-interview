# Log Parsing

> This project was mock interview preparation.

## Summary

I revisited Python concepts like: File I/O in Python, Signal Handling in Python, Data Processing, Regular Expressions, Dictionaries in Python, Exception Handling, etc.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-minoperations.py](https://github.com/Ebube-Ochemba/alx-interview/blob/main/0x03-log_parsing/0-stats.py): Write a script that reads stdin line by line and computes metrics:
  - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
  - After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
    - Total file size: `File size: <total size>`
    - where `<total size>` is the sum of all previous `<file size>` (see input format above)
    - Number of lines by status code:
      - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
      - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
      - format: `<status code>: <number>`
      - status codes should be printed in ascending order

> [0-generator.py](./0-generator.py): A test case for the program. Provided by Alx.
