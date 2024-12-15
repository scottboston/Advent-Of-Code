from scipy.optimize import linprog, milp, LinearConstraint, Bounds
import re
import numpy as np
import aoc_utils.myconfig as utils
input_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2024, 13)

def part1():
    total_spent = 0
    obj = -np.array([3,1])
    bnd = [(l,b) for l, b in zip([0,0],[np.inf,np.inf])]
    l_eqx, l_eqy = [], []
    n=0
    for l in get_input_data(False).strip('\n').splitlines():
        if l == '':
            l_eqx, l_eqy = [], []
            n=0
            continue
        l = l.split(':')[-1]
        if n%3 in [0,1]:
            x, y = re.findall('X.(?P<x>\d+), Y.(?P<y>\d+)',l)[0]
            l_eqx.append(x)
            l_eqy.append(y)
        if n%3 == 2:
            r_eqx, r_eqy = re.findall('X.(?P<x>\d+), Y.(?P<y>\d+)',l)[0]
            A = [l_eqx, l_eqy]
            u_b = [r_eqx, r_eqy]
            constraints = LinearConstraint(A, u_b, u_b)
            opt = milp(c=obj, constraints=constraints, integrality=[1,1])
            total_spent += -opt.fun if opt.success else 0
        n+=1
    result = total_spent
    return result

def part2():
    total_spent = np.float64(0)
    total_arr = []
    obj = -np.array([3,1])
    bnd = [(l,b) for l, b in zip([0,0],[np.inf,np.inf])]
    l_eqx, l_eqy = [], []
    n=0
    for l in get_input_data(False).strip('\n').splitlines():
        if l == '':
            l_eqx, l_eqy = [], []
            n=0
            continue
        l = l.split(':')[-1]
        if n%3 in [0,1]:
            x, y = re.findall('X.(?P<x>\d+), Y.(?P<y>\d+)',l)[0]
            l_eqx.append(np.int64(x))
            l_eqy.append(np.int64(y))
        if n%3 == 2:
            r_eqx, r_eqy = re.findall('X.(?P<x>\d+), Y.(?P<y>\d+)',l)[0]
            A = [l_eqx, l_eqy]
            u_b = [np.int64(r_eqx)+10000000000000, np.int64(r_eqy)+10000000000000]
            constraints = LinearConstraint(A, u_b, u_b)
            opt = milp(c=obj, constraints=constraints, integrality=[1,1])
            total_spent += -opt.fun if opt.success else 0
            total_arr.append(-opt.fun if opt.success else 0)
        n+=1
    result = total_spent, sum(total_arr)
    return result

if __name__ == '__main__':
    print(f'{part1()=}')
    print(f'Not Correct {part2()=}')