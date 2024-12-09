import aoc_utils.myconfig as utils
import pandas as pd
import numpy as np
from itertools import combinations

input_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 8)


def part1():
    input = get_input_data(False)
    a = np.array([[*l] for l in input.splitlines()])
    df = pd.DataFrame(a)
    list_of_antenna = df.mask(df == ".").stack().unique().tolist()
    list_of_antinode = []
    for symbol in list_of_antenna:
        df_sub = df.where(df == symbol).mask(df == ".")
        Ar, Ac = np.where(df_sub == symbol)
        points = list(zip(Ar, Ac))
        for point_a, point_b in list(combinations(points, 2)):
            diff_r = point_a[0] - point_b[0]
            diff_c = point_a[1] - point_b[1]

            new_a_r = point_a[0] + diff_r
            new_a_c = point_a[1] + diff_c
            new_b_r = point_b[0] - diff_r
            new_b_c = point_b[1] - diff_c

            if (
                new_a_r >= 0
                and new_a_r < len(df)
                and new_a_c >= 0
                and new_a_c < len(df)
            ):
                list_of_antinode.append((new_a_r, new_a_c))
            if (
                new_b_r >= 0
                and new_b_r < len(df)
                and new_b_c >= 0
                and new_b_c < len(df)
            ):
                list_of_antinode.append((new_b_r, new_b_c))
    result = len(set(list_of_antinode))
    return result


def part2():
    input = get_input_data(False)
    a = np.array([[*l] for l in input.splitlines()])
    df = pd.DataFrame(a)
    list_of_antenna = df.mask(df == ".").stack().unique().tolist()
    list_of_antinode = []
    for symbol in list_of_antenna:
        df_sub = df.where(df == symbol).mask(df == ".")
        Ar, Ac = np.where(df_sub == symbol)
        points = list(zip(Ar, Ac))
        [list_of_antinode.append(p) for p in points]
        for point_a, point_b in list(combinations(points, 2)):
            diff_r = point_a[0] - point_b[0]
            diff_c = point_a[1] - point_b[1]
            point_a_harmonic = 1
            point_b_harmonic = 1
            while (
                point_a[0] + (diff_r_harmonic := (diff_r * point_a_harmonic)) >= 0
                and point_a[0] + diff_r_harmonic < len(df)
                and point_a[1] + (diff_c_harmonic := (diff_c * point_a_harmonic)) >= 0
                and point_a[1] + diff_c_harmonic < len(df)
            ):
                df_sub.loc[
                    point_a[0] + diff_r_harmonic,
                    point_a[1] + diff_c_harmonic,
                ] = "#"
                list_of_antinode.append(
                    (
                        point_a[0] + diff_r_harmonic,
                        point_a[1] + diff_c_harmonic,
                    )
                )
                point_a_harmonic += 1
            while (
                point_b[0] - (diff_r_harmonic := (diff_r * point_b_harmonic)) >= 0
                and point_b[0] - diff_r_harmonic < len(df)
                and point_b[1] - (diff_c_harmonic := (diff_c * point_b_harmonic)) >= 0
                and point_b[1] - diff_c_harmonic < len(df)
            ):
                df_sub.loc[
                    point_b[0] - diff_r_harmonic,
                    point_b[1] - diff_c_harmonic,
                ] = "#"
                list_of_antinode.append(
                    (
                        point_b[0] - diff_r_harmonic,
                        point_b[1] - diff_c_harmonic,
                    )
                )
                point_b_harmonic += 1
    result = len(set(list_of_antinode))
    return result


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
