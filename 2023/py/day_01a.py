"""
The newly-improved calibration document consists of lines of text; each line originally
contained a specific calibration value that the Elves now need to recover. On each line,
the calibration value can be found by combining the first digit and the last digit (in
that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77.
Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
from typing import Optional


def return_bookend_numbers(input_str: str) -> int:
    if not input_str:
        return 0
    first_digit, last_digit = None, None
    for char in input_str:
        if char.isdigit():
            first_digit = char
            break
    for char in reversed(input_str):
        if char.isdigit():
            last_digit = char
            break
    return int(f"{first_digit}{last_digit}")


def generate_answer(input_override: Optional[str] = None) -> int:
    running_sum = 0
    if input_override:
        for line in input_override.splitlines():
            running_sum += return_bookend_numbers(line.strip())
    else:
        with open("./inputs/day_01.txt") as fin:
            for line in fin.readlines():
                running_sum += return_bookend_numbers(line.strip())
    print(f"Answer to Day 01a is {running_sum}")
    return running_sum

if __name__ == '__main__':
    generate_answer()
