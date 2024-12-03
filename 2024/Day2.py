from io import StringIO
import pandas as pd
import numpy as np
import aoc_utils.myconfig as utils

input_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

input_data = utils.get_data(2024, 2)

def part1():
    a = np.array([l.split() for l in input_data.splitlines()])
    df = pd.DataFrame(a)
    df_t = df.T
    df_t_diff = df_t.diff()
    result = df_t_diff[1:].apply(lambda x: (abs(np.sign(x).sum()) == 4) & (abs(x) <= 3)).all().sum()
    return result

if __name__ == '__main__':
    print(f'{part1()=}')
