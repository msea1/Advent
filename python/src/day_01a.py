"""
As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration
is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks,
rations, etc. that they've brought with them, one item per line. Each Elf separates their own
inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like
to know how many Calories are being carried by the Elf carrying the most Calories. In the example
above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

def find_most_calories_carried(input_str: str) -> int:
    max_calories_seen = 0
    if not input_str:
        return max_calories_seen
    per_elf_list = turn_input_list_into_list_per_elf(input_str)
    for elf_load in per_elf_list:
        elfs_sum = sum(elf_load)
        max_calories_seen = max(max_calories_seen, elfs_sum)
    return max_calories_seen

def turn_input_list_into_list_per_elf(input_str: str) -> list[list[int]]:
    # turn string input into usable data structure
    # first into a list of strings, one per line, including the extra blanks
    # e.g. '1 \n 2 \n 3 \n\n 4 \n 5' -> ['1', '2', '3', '', '4', '5']
    # then coalesce around the extra blanks so that you get one entry per elf
    # e.g. [ [1, 2, 3], [4, 5] ]

    expanded_list = [i.strip() for i in input_str.splitlines()]
    condensed_list = [[]]
    elf_counter = 0
    for entry in expanded_list:
        if entry == "":
            elf_counter += 1
            condensed_list.append([])
        else:
            condensed_list[elf_counter].append(int(entry))
    return condensed_list

def generate_answer() -> None:
    with open("../inputs/day_01a.txt") as fin:
        input = fin.read()
    print(f"Answer to Day 01a is {find_most_calories_carried(input)}")


generate_answer()
