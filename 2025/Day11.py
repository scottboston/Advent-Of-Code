import networkx as nx
from openpyxl.styles.builtins import total

import aoc_utils.myconfig as utils
import igraph as ig
from collections import defaultdict

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
        targetlist.append(target.split(' '))
    for n, s in enumerate(sourcelist):
        [G.add_edge(s, ts) for ts in targetlist[n]]

    paths = nx.all_simple_paths(G, "you", "out")
    return len(list(paths))

def part2():
    G = nx.DiGraph()
    sourcelist = []
    targetlist = []
    for l in input_data.splitlines():
        source, target = l.split(": ")
        sourcelist.append(source)
        targetlist.append(target.split(' '))
    for n, s in enumerate(sourcelist):
        [G.add_edge(s, ts) for ts in targetlist[n]]

    svr_dac = nx.all_simple_paths(G, "svr", "dac")
    return len(list (svr_dac))

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    # print(f"Part 2: {part2()}")
