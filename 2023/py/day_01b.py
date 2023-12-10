"""
Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six, seven,
eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first
and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
"""

from typing import Optional

DIGIT_NAMES = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}


def check_buffer_for_number(buffer: str) -> Optional[int]:
    for digit, num_v in DIGIT_NAMES.items():
        if digit in buffer:
            return num_v
    return None


def check_place_in_string(char: str, buffer: str) -> Optional[int]:
    if char.isdigit():
        return int(char)
    else:
        buffer += char
        if found_num := check_buffer_for_number(buffer):
            return found_num


def return_bookend_numbers(input_str: str) -> int:
    if not input_str:
        return 0
    first_digit, last_digit = None, None
    buffer = ""
    for char in input_str:
        if char.isdigit():
            first_digit = char
            break
        else:
            buffer += char
            if found_num := check_buffer_for_number(buffer):
                first_digit = found_num
                break

    buffer = ""
    for char in reversed(input_str):
        if char.isdigit():
            last_digit = char
            break
        else:
            buffer = char + buffer
            if found_num := check_buffer_for_number(buffer):
                last_digit = found_num
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
    print(f"Answer to Day 01b is {running_sum}")
    return running_sum


if __name__ == '__main__':
    generate_answer()
