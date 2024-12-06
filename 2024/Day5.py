import aoc_utils.myconfig as utils
import networkx as nx
from itertools import combinations

input_data = utils.get_data(year=2024, day=5)
page_order = [l.split("|") for l in input_data.splitlines() if "|" in l]
print_order = [l for l in input_data.splitlines() if "," in l]


def part1():
    G = nx.DiGraph()
    for l in page_order:
        G.add_edge(l[0], l[1])
    print(G)
    mid = []
    for l in print_order:
        l = l.split(",")
        if all(G.has_successor(p, c) for p, c in combinations(l, 2)):
            mid.append(l[len(l) // 2])
    return sum(map(int, mid))


def part2():
    G = nx.DiGraph()
    for l in page_order:
        G.add_edge(l[0], l[1])
    print(G)
    mid = []
    for l in print_order:
        l = l.split(",")
        if all(G.has_successor(p, c) for p, c in combinations(l, 2)):
            pass
        else:
            g = G.subgraph(l)
            l = list(filter(lambda x: x in l, nx.topological_sort(g)))
            mid.append(l[len(l) // 2])
    return sum(map(int, mid))


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")