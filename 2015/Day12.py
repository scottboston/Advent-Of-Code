from unicodedata import numeric
import aoc_utils.myconfig as utils
import re
from ast import literal_eval


def part1():
    input_data = utils.get_data(year=2015, day=12)
    r = re.findall(r"(-?\d+)", input_data)
    total = sum(int(n) for n in r)
    return total


def evaldata(d, accum=0):
    if isinstance(d, int):
        accum += d
    elif isinstance(d, dict):
        if "red" in d.values():
            pass  # found red discard dictionary
        else:
            for e in d.values():
                accum += evaldata(e)
    elif isinstance(d, list):
        for e in d:
            accum += evaldata(e)
    else:
        pass  # found read in list
    return accum


def part2():
    input_data = utils.get_data(year=2015, day=12)
    # input_data = '[1,"red",5]'
    data = literal_eval(input_data)
    return evaldata(data)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
