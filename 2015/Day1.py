import aoc_utils.myconfig as utils

input_data = """(())"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2015, 1)


def part1():
    d = {"(": 1, ")": -1}
    input_data = get_input_data(False)
    floor = sum(d[c] for c in input_data)
    return floor


def part2():
    floor = 0
    d = {"(": 1, ")": -1}
    for stairs, c in enumerate(get_input_data(False), 1):
        floor += d[c]
        if floor == -1:
            return stairs


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
