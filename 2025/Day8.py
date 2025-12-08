import aoc_utils.myconfig as utils
import re
import math
from itertools import combinations
import networkx as nx

input_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

input_data = utils.get_data(2025, 8)

def get_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)


def part1():
    G = nx.Graph()
    circuits = []
    for line in input_data.splitlines():
        circuits.append(re.findall(r'(\d+),(\d+),(\d+)', line)[0])
    circuits = [tuple(map(int, e)) for e in circuits]
    matches = sorted([(a, b) for a, b in combinations(circuits, 2)], key=lambda x: get_distance(*x))[:1000]
    for connection in matches:
        # print(connection)
        G.add_edge(*connection)
        # print(G.nodes)
    ccs = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)][:3]
    return math.prod(ccs)

def part2():
    G = nx.Graph()
    circuits = []
    for line in input_data.splitlines():
        circuits.append(re.findall(r'(\d+),(\d+),(\d+)', line)[0])
    circuits = [tuple(map(int, e)) for e in circuits]
    matches = sorted([(a, b) for a, b in combinations(circuits, 2)], key=lambda x: get_distance(*x))
    i = 0
    while len(G.nodes) < len(circuits):
        G.add_edge(*matches[i])
        i += 1
    last_connection = matches[i-1]
    return last_connection[0][0]*last_connection[1][0]


if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')