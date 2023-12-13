import aoc_utils.myconfig as utils
import numpy as np
from io import StringIO
import pandas as pd
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, Polygon


def part1():
    input_data = utils.get_data(year=2023, day=10)
    a = np.array([[*l] for l in input_data.splitlines()])
    df = pd.DataFrame(a)

    # Add borders around layout
    df.loc[df.shape[0], :] = "."
    df.loc[-1, :] = "."

    df.loc[:, df.shape[1]] = "."
    df.loc[:, -1] = "."

    # Setup directions and pipe segment identifications
    N = (-1, 0)
    W = (0, -1)
    S = (1, 0)
    E = (0, 1)
    direction = [N, W, S, E]
    to_pipes = {
        "F": [S, E],
        "|": [N, S],
        "-": [W, E],
        "J": [N, W],
        "7": [S, W],
        "S": [N, W, S, E],
        "L": [N, E],
        ".": " ",
    }

    r, c = np.where(df.ne("."))
    pipes = dict(enumerate(zip(r, c)))
    ctop = {v: k for k, v in pipes.items()}

    # Use networkx for graph layout
    G = nx.Graph()
    for id, c in pipes.items():
        for d in to_pipes[df.loc[c]]:
            o = c[0] + d[0], c[1] + d[1]
            if df.loc[o] != "." and tuple(map(np.negative, (d))) in to_pipes[df.loc[o]]:
                G.add_edge(ctop[c], ctop[o])

    sloc = ctop[tuple([e[0] for e in np.where(df == "S")])]

    results = max(nx.single_source_shortest_path_length(G, sloc).values())
    return results


def part2():
    input_data = utils.get_data(year=2023, day=10)
    a = np.array([[*l] for l in input_data.splitlines()])
    df = pd.DataFrame(a)

    df.loc[df.shape[0], :] = "."
    df.loc[-1, :] = "."

    df.loc[:, df.shape[1]] = "."
    df.loc[:, -1] = "."

    N = (-1, 0)
    W = (0, -1)
    S = (1, 0)
    E = (0, 1)
    direction = [N, W, S, E]
    passages = {
        "F": {N: E, W: S},
        "|": {N: N, S: S},
        "-": {E: E, W: W},
        "J": {S: W, E: N},
        "7": {N: W, E: S},
        "L": {S: E, W: N},
        ".": dict(),
    }

    r, c = np.where(df == "S")
    loc0 = (r[0], c[0])
    loc0
    G = nx.Graph()

    complete_loop = False
    for d in direction:
        o = loc0
        p = o[0] + d[0], o[1] + d[1]
        try:
            while not complete_loop:
                d = passages[df.loc[p]][d]

                G.add_edge(o, p)
                o, p = p, (p[0] + d[0], p[1] + d[1])
                if p == loc0:
                    print("Found a loop")
                    complete_loop = True
        except KeyError as e:
            print("blocked")
            continue

    polygon_data = {"ID": [1], "geometry": Polygon([Point(y, x) for x, y in G.nodes])}
    polygon_gdf = gpd.GeoDataFrame(polygon_data, geometry="geometry")

    r, c = np.where(df)
    points_data = {"geometry": [Point(y, x) for x, y in zip(r, c)]}
    points_gdf = gpd.GeoDataFrame(points_data, geometry="geometry")

    p_inside = gpd.sjoin(points_gdf, polygon_gdf, how="inner", predicate="within")

    results = p_inside.shape[0]
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
