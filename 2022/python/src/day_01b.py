"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf
carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried
by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of
snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third
Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried
by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""


def find_top_three_calories_carried(input_str: str) -> int:
    # assumption: you cannot have negative calories carried
    top_three_elves = [0, 0, 0]
    if not input_str:
        return sum(top_three_elves)
    # one option would be to sort the list and return up to 3
    # however, sorting incurs an (n ln n) time that I'd like to avoid
    per_elf_totals = turn_input_list_into_sum_per_elf(input_str)
    for elf_load in per_elf_totals:
        top_three_elves = find_placement_within_top_three(top_three_elves, elf_load)
    return sum(top_three_elves)


def turn_input_list_into_sum_per_elf(input_str: str) -> list[int]:
    # turn string input into usable data structure
    # first into a list of strings, one per line, including the extra blanks
    # e.g. '1 \n 2 \n 3 \n\n 4 \n 5' -> ['1', '2', '3', '', '4', '5']
    # then coalesce around the extra blanks, and sum, so that you get one entry per elf
    # e.g. [6, 9]
    expanded_list = [i.strip() for i in input_str.splitlines()]
    condensed_list = [[]]
    elf_counter = 0
    summed = False
    for entry in expanded_list:
        if entry == "":
            condensed_list[elf_counter] = sum(condensed_list[elf_counter])
            elf_counter += 1
            condensed_list.append([])
            summed = True
        else:
            condensed_list[elf_counter].append(int(entry))
            summed = False
    if not summed:
        condensed_list[elf_counter] = sum(condensed_list[elf_counter])
    else:
        condensed_list = condensed_list[:-1]
    return condensed_list


def find_placement_within_top_three(current_top: list[int], potential_entry: int) -> list[int]:
    # assumption: current_top comes in sorted DESC
    if potential_entry < current_top[-1]:
        return current_top
    for i in range(len(current_top)):
        if potential_entry > current_top[i]:
            prefix = current_top[:i]
            prefix.append(potential_entry)
            prefix.extend(current_top[i:-1])
            return prefix


def generate_answer() -> None:
    with open("../inputs/day_01.txt") as fin:
        input = fin.read()
    print(f"Answer to Day 01a is {find_top_three_calories_carried(input)}")


generate_answer()
