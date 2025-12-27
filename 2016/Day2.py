import aoc_utils.myconfig as utils
import numpy as np
from io import StringIO


def part1():
    input_data = utils.get_data(year=2016, day=2)

    arr = np.array(np.arange(1, 10).reshape(3, -1), dtype=object)

    d = {"U": 0 - 1j, "D": 0 + 1j, "R": 1 + 0j, "L": -1 + 0j}
    code = []
    start = 1 + 1j
    newp = nextp = start
    for line in input_data.splitlines():
        for c in line:
            # print(c, nextp, d.get(c))
            newp = newp + d.get(c)
            if newp.real < 0 or newp.real > 2 or newp.imag < 0 or newp.imag > 2:
                newp = nextp
                continue
            nextp = newp
        x = int(nextp.real if nextp.real else 0)
        y = int(nextp.imag if nextp.imag else 0)
        # print(x, y)
        code.append(str(arr[y, x]))
    return "".join(code)


def part2():
    input_data = utils.get_data(year=2016, day=2)

    arr = np.array(
        [
            [np.nan, np.nan, 1, np.nan, np.nan],
            [np.nan, 2, 3, 4, np.nan],
            [5, 6, 7, 8, 9],
            [np.nan, "A", "B", "C", np.nan],
            [np.nan, np.nan, "D", np.nan, np.nan],
        ],
        dtype=object,
    )

    d = {"U": 0 - 1j, "D": 0 + 1j, "R": 1 + 0j, "L": -1 + 0j}
    code = []
    start = 2j
    newp = nextp = start
    for line in input_data.splitlines():
        for c in line:
            # print(c, nextp, d.get(c))
            newp = newp + d.get(c)
            try:
                if (
                    newp.real < 0
                    or newp.real > 4
                    or newp.imag < 0
                    or newp.imag > 4
                    or np.isnan(arr[int(newp.imag), int(newp.real)])
                ):
                    newp = nextp
                    continue
            except Exception as e:
                pass
            nextp = newp
        x = int(nextp.real if nextp.real else 0)
        y = int(nextp.imag if nextp.imag else 0)
        # print(x, y)
        code.append(str(arr[y, x]))
    return "".join(code)


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
