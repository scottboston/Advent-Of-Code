import aoc_utils.myconfig as utils
import numpy as np
import pandas as pd

input_data = utils.get_data(2025, 6)

input_data = """123 32  51 64 
 45 64  387 23 
  6 988  215 314
*   +   *   +  """

input_data = utils.get_data(2025, 6)

def part1():
    worksheet = np.array([l.split() for l in input_data.splitlines()])
    solutions = []
    for c in range(worksheet.shape[1]):
        result = worksheet[:, c]
        if result[-1] == '*':
            solutions.append(np.prod(worksheet[:-1,c].astype(int)))
        else:
            solutions.append(np.sum(worksheet[:-1,c].astype(int)))
    return np.sum(solutions)

def part2():
    worksheet = np.array([[*l] for l in input_data.splitlines()])
    df_problems = pd.DataFrame(worksheet)
    df_problems_T = df_problems.T.iloc[:,::-1]
    problems = df_problems_T.iloc[:,0].ne(' ').cumsum()
    mathfuncs = df_problems_T.iloc[:,0].replace(' ', np.nan).ffill()
    df_problems_T_R = df_problems_T.iloc[:, 1:].iloc[:,::-1]
    df_problem_numbers = df_problems_T_R.sum(axis=1).str.strip().replace('',0).astype(int)
    def columnmath(s):
        if s.iloc[0,-1]  == '*':
            return np.prod(s.iloc[:,0].replace(0,1))
        if s.iloc[0,-1] == '+':
            return np.sum(s.iloc[:,0])
    df = pd.concat([df_problem_numbers, problems, mathfuncs], axis=1)
    result = df.groupby(problems).apply(columnmath).astype(float)
    return result.sum()



if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')

