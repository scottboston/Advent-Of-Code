import aoc_utils.myconfig as utils
from itertools import product
import operator

input_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

input_data = utils.get_data(2024, 7)


def add_string(a, b):
    return str(a) + str(b)


def add_int(a, b):
    return int(a) + int(b)


def mul_int(a, b):
    return int(a) * int(b)


operations = [operator.add, operator.mul]
operations_p2 = [add_int, mul_int, add_string]


def part1():
    total = 0
    for l in input_data.splitlines():
        l = l.split(": ")
        solution = int(l[0])
        numbers = l[1].split(" ")
        operators = product(operations, repeat=len(numbers) - 1)
        for op in operators:
            equation = [int(n) for n in numbers]
            equation = interleave_lists(equation, list(op))
            if eval_func(equation) == solution:
                total += int(solution)
                break
    return total


def eval_func(equation):
    if len(equation) == 1:
        return equation[0]
    equation[0] = equation.pop(1)(equation.pop(0), equation[0])
    return eval_func(equation)


def interleave_lists(list1, list2):
    result = []
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        result.append(list1[i])
        result.append(list2[i])
    if len(list1) > min_length:
        result.extend(list1[min_length:])
    elif len(list2) > min_length:
        result.extend(list2[min_length:])
    return result


def part2():
    total = 0
    for l in input_data.splitlines():
        l = l.split(": ")
        solution = int(l[0])
        numbers = l[1].split(" ")
        operators = product(operations_p2, repeat=len(numbers) - 1)
        for op in operators:
            equation = [int(n) for n in numbers]
            equation = interleave_lists(equation, list(op))
            if eval_func(equation) in [solution, str(solution)]:
                total += solution
                break
    return total


if __name__ == "__main__":
    print(f"{part1()}")
    print(f"{part2()}")
