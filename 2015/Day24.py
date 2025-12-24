import aoc_utils.myconfig as utils
from itertools import chain, combinations
from math import prod

input_data = """1
2
3
4
5
7
8
9
10
11"""

input_data = utils.get_data(year=2015, day=24)

def powerset(iterable):
    "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def part1():
    packages = list(map(int, input_data.splitlines()))
    total_weight = sum(packages)
    group_weight =  total_weight // 3
    list_groups = [p for p in powerset(packages) if sum(p) == group_weight]
    smallest_group = [g for g in list_groups if len(g) == len(list_groups[0])]
    return min(prod(p) for p in smallest_group)

def part2():
    packages = list(map(int, input_data.splitlines()))
    total_weight = sum(packages)
    group_weight =  total_weight // 4
    list_groups = [p for p in powerset(packages) if sum(p) == group_weight]
    smallest_group = [g for g in list_groups if len(g) == len(list_groups[0])]
    return min(prod(p) for p in smallest_group)

if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
