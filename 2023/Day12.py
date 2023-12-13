import aoc_utils.myconfig as utils
import pandas as pd
import re


def part1():
    input_data = utils.get_data(year=2023, day=12)
    total = 0
    for lines in input_data.splitlines():
        record, condition = lines.split(" ")
        n = record.count("?")
        record = record.replace("?", "{}")
        mapping = str.maketrans("01", ".#")
        for i in range(2**n):
            b = bin(i)[2:].zfill(n)
            pat_trans = b.translate(mapping)
            r = record.format(*pat_trans)
            l = [str(e.group().count("#")) for e in re.finditer(r"([#])(\1*)", r)]
            if l == condition.split(","):
                total += 1
    results = total
    return results


def part2():
    input_data = utils.get_data(year=2023, day=12)
    results = None
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
