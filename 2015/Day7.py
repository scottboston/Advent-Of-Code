import networkx as nx
from itertools import permutations
import aoc_utils.myconfig as utils





def part1():
    operations = {}
    results = {}
    input_data = utils.get_data(year=2015, day=7)
    for command in input_data.splitlines():
        operation, result = command.split(' -> ')
        operations[result] = operation.split(' ')

    def eval_operation(expression):
        try:
            return int(expression)
        except Exception:
            pass

        if expression not in results:
            operation = operations[expression]
            if len(operation) == 1:
                result = eval_operation(operation[0])
            else:
                op = operation[-2]
                if op == "AND":
                    result = eval_operation(operation[0]) & eval_operation(operation[2])
                elif op == "OR":
                    result = eval_operation(operation[0]) | eval_operation(operation[2])
                elif op == "NOT":
                    result = ~eval_operation(operation[1]) & 0xffff
                elif op == "RSHIFT":
                    result = eval_operation(operation[0]) >> eval_operation(operation[2])
                elif op == "LSHIFT":
                    result = eval_operation(operation[0]) << eval_operation(operation[2])
                else:
                    print('oopsy')
            results[expression] = result
        return results[expression]

    return eval_operation('a')

def part2():
    operations = {}
    results = {}
    input_data = utils.get_data(year=2015, day=7)
    for command in input_data.splitlines():
        operation, result = command.split(' -> ')
        operations[result] = operation.split(' ')

    #Override
    operations['b'] = [part1()]

    def eval_operation(expression):
        try:
            return int(expression)
        except Exception:
            pass

        if expression not in results:
            operation = operations[expression]
            if len(operation) == 1:
                result = eval_operation(operation[0])
            else:
                op = operation[-2]
                if op == "AND":
                    result = eval_operation(operation[0]) & eval_operation(operation[2])
                elif op == "OR":
                    result = eval_operation(operation[0]) | eval_operation(operation[2])
                elif op == "NOT":
                    result = ~eval_operation(operation[1]) & 0xffff
                elif op == "RSHIFT":
                    result = eval_operation(operation[0]) >> eval_operation(operation[2])
                elif op == "LSHIFT":
                    result = eval_operation(operation[0]) << eval_operation(operation[2])
                else:
                    print('oopsy')
            results[expression] = result
        return results[expression]

    return eval_operation('a')


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
