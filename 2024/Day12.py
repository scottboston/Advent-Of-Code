import pandas as pd
import numpy as np
import geopandas as gp
from shapely import unary_union, simplify

import aoc_utils.myconfig as utils
from shapely.geometry import Point, Polygon, MultiPolygon
from functools import reduce

input_data = """AAAA
BBCD
BBCC
EEEC"""

# input_data = """OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO"""

# input_data = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 12)


def part1():
    a = np.array([[*l] for l in get_input_data(False).splitlines()])
    df = pd.DataFrame(a)
    corners = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)]
    areas = df.stack().unique()
    total_price = 0
    total_price_2 = 0
    for a in areas:
        pr, pc = np.where(df == a)
        newp = []
        for x, y in zip(pr, pc):
            newp.append(Polygon([Point(y + c[0], x + c[1]) for c in corners]))
        newp = MultiPolygon(newp)
        newp = unary_union(newp)
        total_price += (
            sum(p.length * p.area for p in newp.geoms)
            if isinstance(newp, MultiPolygon)
            else newp.length * newp.area
        )
        newp = simplify(newp, 0.1, True)
        # total_price_2 += sum((len(set(newp.boundary.coords))-1)*p.area for p in newp.geoms) if isinstance(newp, MultiPolygon) else (len(set(newp.boundary.coords))-1)*newp.area
    result = total_price
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
