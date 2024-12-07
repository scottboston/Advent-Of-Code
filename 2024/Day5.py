import aoc_utils.myconfig as utils
import networkx as nx
from itertools import combinations

input_data = utils.get_data(year=2024, day=5)
page_order = [line.split("|") for line in input_data.splitlines() if "|" in line]
print_order = [line for line in input_data.splitlines() if "," in line]


def part1_and_part2():
    G = nx.DiGraph()
    for pages in page_order:
        G.add_edge(pages[0], pages[1])
    print(G)
    part1_mid = []
    part2_mid = []
    for pages in print_order:
        pages = pages.split(",")
        if all(G.has_successor(p, c) for p, c in combinations(pages, 2)):
            part1_mid.append(pages[len(pages) // 2])
        else:
            g = G.subgraph(pages)
            pages = list(nx.topological_sort(g))
            part2_mid.append(pages[len(pages) // 2])
    return sum(map(int, part1_mid)), sum(map(int, part2_mid))


if __name__ == "__main__":
    print(f"{part1_and_part2()=}")
