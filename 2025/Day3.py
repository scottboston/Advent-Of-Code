import aoc_utils.myconfig as utils

input_data = """987654321111111
811111111111119
234234234234278
818181911112111"""

input_data = utils.get_data(2025, 3)


def part1():
    joltage_total = 0
    for l in input_data.splitlines():
        first = max(l[:-1])
        idx = l.index(first)
        second = max(l[idx + 1 :])
        joltage_total += int("".join([first, second]))
    return joltage_total


def part2():
    joltage_total = 0
    for l in input_data.splitlines():
        battery = []
        first = max(l[:-11])
        battery.append(first)
        idx = l.index(first)
        for i in range(2, 13):
            next_digit = max(l[idx + 1 : len(l) - 12 + i])
            battery.append(next_digit)
            idx = l.index(next_digit, idx + 1)
        joltage_total += int("".join(battery))
    return joltage_total


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
