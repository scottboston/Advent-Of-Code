import aoc_utils.myconfig as utils
import numpy as np
import networkx as nx
import pandas as pd
import re
from itertools import combinations
from collections import deque

input_data = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

# input_data = """x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1
#
# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj"""



def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 24)

values = [l.split(': ') for l in get_input_data(False).splitlines() if ':' in l]
gates = [l.split(' -> ') for l in get_input_data(False).splitlines() if '->' in l]
d_values = {k:int(v) for k, v in values}

def part1():
    for g in gates:
        d_values[g[1]] = g[0]
    result = [evaluate(left) for left,right in reversed(sorted(gates, key=lambda x: x[-1][-2:])) if right[0] == 'z']
    return int(''.join(map(str, result)), 2)

def evaluate(eq):
    if eq in [0,1]:
        return eq
    if ' ' not in eq:
        return evaluate(d_values[eq])
    op1, operator, op2 = eq.split(' ')
    if operator == 'AND':
        return evaluate(op1) & evaluate(op2)
    elif operator == 'OR':
        return evaluate(op1) | evaluate(op2)
    else:
        return evaluate(op1) ^ evaluate(op2)


if __name__ == '__main__':
    print(f'{part1()=}')