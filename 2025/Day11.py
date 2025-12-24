import networkx as nx
import aoc_utils.myconfig as utils
from collections import defaultdict
from functools import cache

input_data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

input_data = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

input_data = utils.get_data(2025, 11)


def part1():
    G = nx.DiGraph()
    sourcelist = []
    targetlist = []
    for l in input_data.splitlines():
        source, target = l.split(": ")
        sourcelist.append(source)
        targetlist.append(target.split(" "))
    for n, s in enumerate(sourcelist):
        [G.add_edge(s, ts) for ts in targetlist[n]]

    paths = nx.all_simple_paths(G, "you", "out")
    return len(list(paths))


def part1a():
    def parse_moves(input_data):
        dd = defaultdict(list)
        for line in input_data.splitlines():
            key, moves = line.split(": ")
            moves = moves.split()
            for move in moves:
                dd[key].append(move)
        return dd

    def sum_paths(start, end, dd):
        if start == end:
            return 1
        return sum(sum_paths(n, end, dd) for n in dd[start])

    return sum_paths("you", "out", parse_moves(input_data))


def part2():
    """Find this way of solving this solution using frozenset to memoize the sum_paths function"""
    dd = {}

    for l in input_data.splitlines():
        key, moves = l.split(": ")
        dd[key] = moves.split(" ")

    @cache
    def sum_paths(start, finish, required):
        if start == finish:
            return 1 if not required else 0
        total = 0
        for mid in dd[start]:
            new_required = required - {start}
            total += sum_paths(mid, finish, new_required)
        return total

    return sum_paths("svr", "out", frozenset({"dac", "fft"}))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 1a: {part1a()}")
    print(f"Part 2: {part2()}")
