import functools
import copy
import re
from typing import Tuple, List

Docks = List[List[str]]
Ops = List[Tuple[int, int, int]]


@functools.cache
def read_input(file_name: str) -> Tuple[Docks, Ops]:
    with open(f"./inputs/{file_name}.txt") as f:
        crane_defs, op_defs = [p.split("\n") for p in f.read().split("\n\n")]

    docks = [list() for _ in range(int(crane_defs.pop().split(" ")[-1]))]
    for crane_def in crane_defs:
        i = 0
        while crane_def:  # I am not doing non-trivial regexes on my birthday as my religion dictates sorry
            component, crane_def = crane_def[:3].strip(), crane_def[4:]
            if component:
                docks[i].append(component.replace("[", "").replace("]", ""))
            i += 1

    op_regex = re.compile(r"(\d+)")
    ops = [tuple(int(find) for find in op_regex.findall(op_def)) for op_def in op_defs]
    return docks, ops


def execute_ops(docks: Docks, ops: Ops,
                is_superior_crate_mover_9001_meaning_it_can_actually_lift_multiple_crates_at_the_same_time=False) -> Docks:
    docks = copy.deepcopy(docks)

    for n_cranes, origin, destination in ops:
        origin, destination = origin - 1, destination - 1
        selected_cranes = docks[origin][:n_cranes]
        if not is_superior_crate_mover_9001_meaning_it_can_actually_lift_multiple_crates_at_the_same_time:
            selected_cranes = selected_cranes[::-1]
        docks[destination] = selected_cranes + docks[destination]
        del docks[origin][:n_cranes]

    return docks


def part_1(file_name: str) -> str:
    end_docks = execute_ops(*read_input(file_name),
                            is_superior_crate_mover_9001_meaning_it_can_actually_lift_multiple_crates_at_the_same_time=False)
    return "".join(dock[0] for dock in end_docks)


def part_2(file_name: str) -> str:
    end_docks = execute_ops(*read_input(file_name),
                            is_superior_crate_mover_9001_meaning_it_can_actually_lift_multiple_crates_at_the_same_time=True)
    return "".join(dock[0] for dock in end_docks)


for file_name in ["test", "real"]:
    print(f"Part 1: {part_1(file_name)}")
    print(f"Part 2: {part_2(file_name)}")
