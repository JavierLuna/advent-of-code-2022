import functools
from typing import Tuple, List

Sector = Tuple[int, int]
SectorPair = Tuple[Sector, Sector]


@functools.cache
def read_sectors(file_name: str) -> List[SectorPair]:
    with open(f"./inputs/{file_name}.txt") as f:
        return [tuple(tuple(int(sector) for sector in elf.split("-")) for elf in line.strip().split(",")) for line in f]


def part_1(file_name: str) -> int:
    return sum(int((min(s1[0], s2[0]), max(s1[1], s2[1])) in {s1, s2}) for s1, s2 in read_sectors(file_name))


def part_2(file_name: str) -> int:
    return sum(int(int(max(s1[0], s2[0]) <= min(s1[-1], s2[-1]))) for s1, s2 in read_sectors(file_name))


for file_name in ["test", "real"]:
    print(f"Part 1: {part_1(file_name)}")
    print(f"Part 2: {part_2(file_name)}")
