import aoc_utils.myconfig as utils
import numpy as np
import networkx as nx
import pandas as pd
from itertools import permutations, combinations_with_replacement


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 19)


input_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def part1():
    data = get_input_data(False).strip("\n").splitlines()
    resources = data[0].split(", ")
    patterns = data[2:]
    print(f"{resources=}-{len(resources)=}")
    print(f"{patterns=}")

    total = 0
    for towel in patterns:
        # Quick checks
        if towel[0] not in [c[0] for c in resources] or towel[-1] not in [
            c[-1] for c in resources
        ]:
            print(f"{towel=} is not feasible")
            continue

        # Short to use only resources found in towel
        shorten_resources = [c for c in resources if c in towel]
        n = len(towel)

        # Check each letter of towel to see if a resource fits in he next few letters
        findstr = [False] * (n + 1)
        findstr[0] = True
        for i in range(n):
            if not findstr[i]:
                continue
            for r in shorten_resources:
                if i + len(r) <= n and towel[i : i + len(r)] == r:
                    findstr[i + len(r)] = True

        total += findstr[-1]
    result = total
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
