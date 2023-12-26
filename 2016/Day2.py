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


if __name__ == "__main__":
    print(f"{part1()=}")
