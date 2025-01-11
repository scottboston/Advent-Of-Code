import aoc_utils.myconfig as utils
import re


def get_input_data(testdata: bool = True) -> str:
    if testdata:
        return input_data
    else:
        return utils.get_data(2015, 16)


ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def part1():
    for l in get_input_data(False).splitlines():
        sue_no = re.findall(r"Sue (\d+)", l)[0]
        children = re.findall(r"children: (\d+)", l)
        cats = re.findall(r"cats: (\d+)", l)
        samoyeds = re.findall(r"samoyeds: (\d+)", l)
        pomeranians = re.findall(r"pomeranians: (\d+)", l)
        akitas = re.findall(r"akitas: (\d+)", l)
        vizslas = re.findall(r"vizslas: (\d+)", l)
        goldfish = re.findall(r"goldfish: (\d+)", l)
        trees = re.findall(r"trees: (\d+)", l)
        cars = re.findall(r"cars: (\d+)", l)
        perfumes = re.findall(r"perfumes: (\d+)", l)
        if children and int(children[0]) != ticker_tape["children"]:
            continue
        if cats and int(cats[0]) != ticker_tape["cats"]:
            continue
        if samoyeds and int(samoyeds[0]) != ticker_tape["samoyeds"]:
            continue
        if pomeranians and int(pomeranians[0]) != ticker_tape["pomeranians"]:
            continue
        if akitas and int(akitas[0]) != ticker_tape["akitas"]:
            continue
        if vizslas and int(vizslas[0]) != ticker_tape["vizslas"]:
            continue
        if goldfish and int(goldfish[0]) != ticker_tape["goldfish"]:
            continue
        if trees and int(trees[0]) != ticker_tape["trees"]:
            continue
        if cars and int(cars[0]) != ticker_tape["cars"]:
            continue
        if perfumes and int(perfumes[0]) != ticker_tape["perfumes"]:
            continue
        return sue_no
    return None


def part2():
    for l in get_input_data(False).splitlines():
        sue_no = re.findall(r"Sue (\d+)", l)[0]
        children = re.findall(r"children: (\d+)", l)
        cats = re.findall(r"cats: (\d+)", l)
        samoyeds = re.findall(r"samoyeds: (\d+)", l)
        pomeranians = re.findall(r"pomeranians: (\d+)", l)
        akitas = re.findall(r"akitas: (\d+)", l)
        vizslas = re.findall(r"vizslas: (\d+)", l)
        goldfish = re.findall(r"goldfish: (\d+)", l)
        trees = re.findall(r"trees: (\d+)", l)
        cars = re.findall(r"cars: (\d+)", l)
        perfumes = re.findall(r"perfumes: (\d+)", l)
        if children and int(children[0]) != ticker_tape["children"]:
            continue
        if cats and int(cats[0]) <= ticker_tape["cats"]:
            continue
        if pomeranians and int(pomeranians[0]) >= ticker_tape["pomeranians"]:
            continue
        if samoyeds and int(samoyeds[0]) != ticker_tape["samoyeds"]:
            continue
        if akitas and int(akitas[0]) != ticker_tape["akitas"]:
            continue
        if vizslas and int(vizslas[0]) != ticker_tape["vizslas"]:
            continue
        if goldfish and int(goldfish[0]) >= ticker_tape["goldfish"]:
            continue
        if trees and int(trees[0]) <= ticker_tape["trees"]:
            continue
        if cars and int(cars[0]) != ticker_tape["cars"]:
            continue
        if perfumes and int(perfumes[0]) != ticker_tape["perfumes"]:
            continue
        print(l)
        return sue_no
    return None


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
