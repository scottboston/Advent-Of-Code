import networkx as nx
from itertools import permutations
import aoc_utils.myconfig as utils

def part1():
    input_data = utils.get_data(year=2015, day=8)
    raw = 0
    reg = 0
    for line in input_data.splitlines():
        raw += len(line)
        reg += len(eval(line))
    results = raw - reg
    return results

def part2():
    input_data = utils.get_data(year=2015, day=8)
    raw = 0
    reg = 0
    enc = 0
    for line in input_data.splitlines():
        raw += len(line)
        reg += len(eval(line))
        enc += len(line.replace('\\', '\\\\').replace('"', r'\"'))+2
    results = enc - raw
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
