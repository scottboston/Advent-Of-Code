import networkx as nx
from itertools import permutations
import aoc_utils.myconfig as utils


def part1():
    input_data = utils.get_data(year=2015, day=9)

    G = nx.Graph()
    for line in input_data.splitlines():
        f_city, t_city_weight = line.split(" to ")
        t_city, weight = t_city_weight.split(" = ")
        G.add_edge(f_city, t_city, weight=int(weight))

    results = min(
        nx.path_weight(G, p, "weight")
        for p in list(permutations(G.nodes, len(G.nodes)))
    )
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
