import aoc_utils.myconfig as utils
import re

input_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

input_data = utils.get_data(2020, 2)


def part1():
    total = 0
    for line in input_data.splitlines():
        lowest, highest, letter, password = re.findall(
            r"(\d+)-(\d+) (\w): (\w+)", line
        )[0]
        if int(lowest) <= password.count(letter) <= int(highest):
            total += 1
    return total


def part2():
    total = 0
    for line in input_data.splitlines():
        lowest, highest, letter, password = re.findall(
            r"(\d+)-(\d+) (\w): (\w+)", line
        )[0]
        lowest, highest = int(lowest), int(highest)
        letter1 = password[lowest - 1] == letter
        letter2 = password[highest - 1] == letter
        if letter1 ^ letter2:
            total += 1
    return total


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
