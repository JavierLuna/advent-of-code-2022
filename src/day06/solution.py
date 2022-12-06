from typing import List

DataBuffer = List[str]

def read_input(file_name) -> DataBuffer:
    with open(f"./inputs/{file_name}.txt") as f:
        return list(f.read().strip())


def seek_start_marker(buff: DataBuffer, n_different) -> int:
    for i in range(0, len(buff) - n_different):
        if len(set(buff[i:i + n_different])) == n_different:
            return i + n_different


for file_name in ["test", "real"]:
    buff = read_input(file_name)
    print(f"Part 1: {seek_start_marker(buff, 4)}")
    print(f"Part 2: {seek_start_marker(buff, 14)}")
