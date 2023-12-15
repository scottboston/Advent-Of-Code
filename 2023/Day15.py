import aoc_utils.myconfig as utils
from itertools import combinations
import pandas as pd
import numpy as np
from io import StringIO

def get_word_value(word: str):
    hvalue = 0
    for c in word:
        v = ord(c)
        hvalue += v
        hvalue *= 17
        hvalue %= 256
    return hvalue

def part1():
  input_data = utils.get_data(year=2023, day=15)
  results = sum(map(get_word_value, input_data.split(',')))
  return results
  
def part2():
  input_data = utils.get_data(year=2023, day=15)

  box = {key: {} for key in range(256)}

  for label in input_data.split(','):
      if '=' in label:
          box_label = label.split('=')[0]
          box_num = get_word_value(box_label)
          box[box_num] |= dict([tuple(label.split('='))])
      else:
          box_label = label.split('-')[0]
          box_num = get_word_value(box_label)
          if box[box_num].get(box_label):
              del box[box_num][box_label]
  results = sum((k+1)*n*int(d) for k in box for n,d in enumerate(box[k].values(), 1))
  return results

if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
