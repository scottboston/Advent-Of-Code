import aoc_utils.myconfig as utils
import numpy as np
import networkx as nx
from math import prod


def part1():
    input_data = utils.get_data(year=2023, day=25)
    G = nx.Graph()
    for line in input_data.splitlines():
        f_node, t_nodes = line.split(": ")
        for node in t_nodes.split(" "):
            G.add_edge(f_node, node)

    cut_edges = nx.minimum_edge_cut(G)
    G.remove_edges_from(cut_edges)
    results = prod([len(c) for c in nx.connected_components(G)])
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
