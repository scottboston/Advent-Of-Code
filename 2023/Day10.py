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
    passages = {
        "F": {S: E, E: S},
        "|": {N: S, S: N},
        "-": {W: E, E: W},
        "J": {N: W, W: N},
        "7": {S: W, W: S},
        "L": {N: E, E: N},
        ".": {},
    }

    r, c = np.where(df.ne("."))
    pipes = dict(enumerate(zip(r, c)))
    ctop = {v: k for k, v in pipes.items()}

    r, c = np.where(df == "S")
    p = (r[0], c[0])

    G = nx.Graph()

    run = True
    for d in direction:
        o = p[0] + d[0], p[1] + d[1]
        print(o, df.loc[o], passages[df.loc[o]], d, tuple(map(np.negative, (d))))
        try:
            while run:
                d = passages[df.loc[o]][tuple(map(np.negative, (d)))]
                # print(f'Adding Edge {ctop[o]} - {ctop[p]}')
                G.add_edge(ctop[o], ctop[p])
                p = o
                o = p[0] + d[0], p[1] + d[1]
                if p == (r[0], p[0]):
                    run = False
        except KeyError:
            print("blocked")
            continue

    polygon_data = {
        "ID": [1],
        "geometry": Polygon([Point(x, y) for x, y in [pipes[p] for p in G.nodes]]),
    }
    polygon_gdf = gpd.GeoDataFrame(polygon_data, geometry="geometry")

    r, c = np.where(df)
    points_data = {"geometry": [Point(x, y) for x, y in zip(r, c)]}
    points_gdf = gpd.GeoDataFrame(points_data, geometry="geometry")

    p_inside = gpd.sjoin(points_gdf, polygon_gdf, how="inner", predicate="within")
    results = p_inside.shape[0]

    # Returning incorrect number four short of actual number

    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")  # Not correct
