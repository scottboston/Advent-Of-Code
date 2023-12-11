import aoc_utils.myconfig as utils
from itertools import combinations
import pandas as pd
import numpy as np
from io import StringIO

def part1():
  input_string = utils.get_data(year=2023, day=11)
  df = pd.read_csv(StringIO(input_data), header=None)
  df = df[0].apply(lambda x: pd.Series([*x]))
  dfm = df.mask(df.eq('.'))
  
  df = df.reindex(df.index.repeat(dfm.isna().all(1).add(1)))
  df = df.reindex(df.columns.repeat(dfm.isna().all().add(1)), axis=1)
  
  r,c = np.where(df.eq('#'))
  
  def ptp(a: tuple, b:tuple):
      x_diff = abs(a[0]-b[0])
      y_diff = abs(a[1]-b[1])
      return x_diff + y_diff

  results = sum(ptp(a, b) for a, b in combinations(zip(r, c), 2))
  return results
  
def part2():
  input_string = utils.get_data(year=2023, day=11)
  results = None
  return results

if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
