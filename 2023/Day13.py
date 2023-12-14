import aoc_utils.myconfig as utils
import numpy as np


def test_col_mirror(arr):
    cs = np.where((arr[:, :-1] == arr[:, 1:]).all(0))[0]
    for c in cs.tolist():
        i = c + 1
        il, ih = split_index(arr.shape[1], i)
        tr = arr[:, il] == np.fliplr(arr[:, ih])
        if tr.all():
            return c + 1
    return 0


def test_row_mirror(arr):
    cs = np.where((arr[:-1, :] == arr[1:, :]).all(1))[0]
    for c in cs.tolist():
        i = c + 1
        il, ih = split_index(arr.shape[0], i)
        tr = arr[il, :] == np.flipud(arr[ih, :])
        if tr.all():
            return c + 1
    return 0


def split_index(max, s):
    if s < max / 2:
        ll, hl = (0, s)
        hl, hh = (s, s + s)
    elif s > max / 2:
        ll, hl = (s - (max - s), s)
        hl, hh = (s, max)
    else:
        ll, hl = 0, s
        hl, hh = s, max
    return np.arange(max)[ll:hl], np.arange(max)[hl:hh]


def part1():
    input_data = utils.get_data(year=2023, day=13)
    frames = {}
    frame_number = 0

    for lines in input_data.splitlines():
        if len(lines) == 0:
            frame_number += 1
            continue
        if frames.get(frame_number):
            frames[frame_number].append(lines)
        else:
            frames[frame_number] = [lines]

    r_total = 0
    c_total = 0
    for _, frame in frames.items():
        arr = np.array([[*line] for line in frame], dtype=object)
        r_total += test_row_mirror(arr)
        c_total += test_col_mirror(arr)
    results = r_total * 100 + c_total
    return results


def part2():
    input_data = utils.get_data(year=2023, day=13)
    results = None
    return results


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
