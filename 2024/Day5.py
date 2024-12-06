import aoc_utils.myconfig as utils
import networkx as nx
from itertools import combinations

input_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

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
    print(mid)
    return sum(map(int, mid))


if __name__ == "__main__":
    print(f"{part1()=}")
