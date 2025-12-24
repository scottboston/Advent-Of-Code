import aoc_utils.myconfig as utils
import re
from math import prod
from itertools import combinations

input_data = utils.get_data(year=2015, day=2)

def part1():
    total = 0
    for line in input_data.splitlines():
        dims = list(map(int, re.findall(r"\d+", line)))
        total += sum(prod(i)*2 for i in combinations(dims, 2)) + min(prod(i) for i in combinations(dims, 2))
    return total

def part2():
    total = 0
    for line in input_data.splitlines():
        dims = list(map(int, re.findall(r"\d+", line)))
        dims.sort()
        total += (prod(dims) + 2 * dims[0] + 2 * dims[1])
    return total

if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
