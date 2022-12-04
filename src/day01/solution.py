import functools
from typing import List


@functools.cache
def read_elf_cals(file_name: str) -> List[int]:
    elf_cals = [0]
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if not line:
                elf_cals.append(0)
            else:
                elf_cals[-1] += int(line)
    return sorted(elf_cals)


def sum_topn_elfs(file_name: str, n: int) -> int:
    return sum(sorted(read_elf_cals(file_name), reverse=True)[:n])


def part1(file_name: str):
    print(sum_topn_elfs(file_name, 1))


def part2(file_name: str):
    print(sum_topn_elfs(file_name, 3))


for file_name in ["test.txt", "real.txt"]:
    part1(f"./inputs/{file_name}")
    part2(f"./inputs/{file_name}")
