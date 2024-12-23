import aoc_utils.myconfig as utils
import numpy as np
import networkx as nx
import pandas as pd
import re
from itertools import combinations
import pypeln as pl

input_data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 23)


def part1():
    pat = "([a-z]{2})-([a-z]{2})"
    G = nx.Graph()
    for l in get_input_data(False).splitlines():
        matches = re.findall(pat, l)
        source, target = matches[0]
        G.add_edge(source, target)
    s = set()
    for v in G.nodes:
        for u in G.neighbors(v):
            for w in G.neighbors(u):
                if w in G.neighbors(v):
                    if "t" in [v[0], u[0], w[0]]:
                        s.add(tuple(sorted([v, u, w])))
    return len(s)


def part2():
    pat = "([a-z]{2})-([a-z]{2})"
    G = nx.Graph()
    for l in get_input_data(False).splitlines():
        matches = re.findall(pat, l)
        source, target = matches[0]
        G.add_edge(source, target)
    cli = nx.node_clique_number(G)
    comps = sorted([k for k, v in cli.items() if v == max(cli.values())])
    return ",".join(comps)


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
