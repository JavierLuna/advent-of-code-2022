import functools

from typing import List, Tuple

EncryptedStrategy = List[Tuple[str, str]]


@functools.cache
def get_score(opponent: str, me: str) -> int:
    me_index = "XYZ".index(me)
    return me_index + 1 + ["BAC", "CBA", "ACB"][me_index].index(opponent) * 3


@functools.cache
def get_my_hand(opponent: str, scenario: str) -> str:
    return ["ZXY", "XYZ", "YZX"]["XYZ".index(scenario)]["ABC".index(opponent)]


def part_1(content: EncryptedStrategy) -> int:
    return sum(get_score(opponent, you) for opponent, you in content)


def part_2(content: EncryptedStrategy) -> int:
    return sum(get_score(opponent, get_my_hand(opponent, scenario)) for opponent, scenario in content)


for file_name in ["test", "real"]:
    with open(f"./inputs/{file_name}.txt") as f:
        strategy: EncryptedStrategy = [tuple(l.strip().split(" ")) for l in f]

    print(f"Part 1: {part_1(strategy)}")
    print(f"Part 2: {part_2(strategy)}")
