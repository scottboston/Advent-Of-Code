import aoc_utils.myconfig as utils
import re

input_data = utils.get_data(year=2015, day=23)

# input_data = """inc a
# jio a, +2
# tpl a
# inc a"""

def part1():
    registers = {'a': 0, 'b': 0}
    instruction = []
    register = []
    offset = []
    for line in input_data.splitlines():
        instruction.append(line.split()[0])
        register.append(re.findall(r'([ab])', line.rsplit(' ')[1]))
        offset.append(re.findall(r'([+-]\d+)', line.rsplit(' ', maxsplit=1)[1]))
        # print(instruction, register, offset)
    i = 0
    while (i < len(instruction)):
        if instruction[i] == 'hlf':
            registers[register[i][0]] /= 2
        if instruction[i] == 'tpl':
            registers[register[i][0]] *= 3
        if instruction[i] == 'inc':
            registers[register[i][0]] += 1
        if instruction[i] == 'jmp':
            i += int(offset[i][0])-1
        if instruction[i] == 'jie':
            if registers[register[i][0]] % 2 == 0:
                i += int(offset[i][0])-1
        if instruction[i] == 'jio':
            if registers[register[i][0]] == 1:
                i += int(offset[i][0])-1
        i += 1
    return registers['b']

def part2():
    registers = {'a': 1, 'b': 0}
    instruction = []
    register = []
    offset = []
    for line in input_data.splitlines():
        instruction.append(line.split()[0])
        register.append(re.findall(r'([ab])', line.rsplit(' ')[1]))
        offset.append(re.findall(r'([+-]\d+)', line.rsplit(' ', maxsplit=1)[1]))

    i = 0
    while (i < len(instruction)):
        if instruction[i] == 'hlf':
            registers[register[i][0]] /= 2
        if instruction[i] == 'tpl':
            registers[register[i][0]] *= 3
        if instruction[i] == 'inc':
            registers[register[i][0]] += 1
        if instruction[i] == 'jmp':
            i += int(offset[i][0])-1
        if instruction[i] == 'jie':
            if registers[register[i][0]] % 2 == 0:
                i += int(offset[i][0])-1
        if instruction[i] == 'jio':
            if registers[register[i][0]] == 1:
                i += int(offset[i][0])-1
        i += 1
    return registers['b']


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")