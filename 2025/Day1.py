import aoc_utils.myconfig as utils

input_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

input_data = utils.get_data(2025, 1)


def part1():
    zeros = 0
    dial = 50
    for l in input_data.splitlines():
        clicks = int(l[1:])
        if l[0] == "L":
            dial -= clicks
        elif l[0] == "R":
            dial += clicks
        dial = dial % 100
        if dial == 0:
            zeros += 1
    return zeros


def part2():
    zeros = 0
    dial = 50
    for l in input_data.splitlines():
        clicks = int(l[1:])
        if l[0] == "L":
            m = -1
            for i in range(1, clicks + 1):
                if ((dial - i) % 100) == 0:
                    zeros += 1
        if l[0] == "R":
            m = 1
            for i in range(1, clicks + 1):
                if ((dial + i) % 100) == 0:
                    zeros += 1
        dial += clicks * m
        dial %= 100
    return zeros


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
