import aoc_utils.myconfig as utils
import re


def part1():
    input_data = utils.get_data(year=2023, day=4)
    results = sum(
        int(
            2
            ** (
                len(
                    set.intersection(*map(lambda x: set(x.split()), l[8:].split(" | ")))
                )
                - 1
            )
        )
        for l in input_data.split("\n")
    )
    return results


def part2():
    input_data = utils.get_data(year=2023, day=4)
    lines = input_data.split("\n")
    card_count = {n: 1 for n in range(1, len(lines) + 1)}
    for n, l in enumerate(lines, 1):
        matches = len(
            set.intersection(*map(lambda x: set(x.split()), l[8:].split(" | ")))
        )
        for c in range(1, matches + 1):
            card_count[c + n] += card_count[n]
    results = sum(card_count.values())
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
