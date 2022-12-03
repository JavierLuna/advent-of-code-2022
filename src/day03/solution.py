from typing import Tuple, List, Set
import string

RuckSack = Tuple[Set[str], Set[str]]
VALUES = {c: i for i, c in enumerate(string.ascii_letters)}


def read_rucksacks(file_name: str) -> List[RuckSack]:
    halve_str = lambda s: (set(s[:len(s) // 2]), set(s[len(s) // 2:]))
    with open(f"./inputs/{file_name}.txt") as f:
        return [halve_str(l.strip()) for l in f]


def part_1(file_name: str) -> int:
    return sum(VALUES[r1.intersection(r2).pop()] for r1, r2 in read_rucksacks(file_name))


def part_2(file_name: str) -> int:
    rucksacks = read_rucksacks(file_name)
    value = 0
    while rucksacks:
        group, rucksacks = rucksacks[:3], rucksacks[3:]
        group = [r1.union(r2) for r1, r2 in group]
        value += VALUES[group[0].intersection(group[1]).intersection(group[2]).pop()]

    return value


for file_name in ["test", "real"]:
    print(f"Part 1: {part_1(file_name)}")
    print(f"Part 2: {part_2(file_name)}")
