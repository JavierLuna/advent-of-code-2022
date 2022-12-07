import functools
from abc import abstractmethod, ABCMeta
from typing import List


class FSNode(metaclass=ABCMeta):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_size(self) -> int:
        pass


class Directory(FSNode):
    def __init__(self, name: str, parent):
        super().__init__(name)
        self.parent = parent
        self._nodes: List[FSNode] = []
        self._cached_size = None

    def add_node(self, node: FSNode):
        self._nodes.append(node)
        self._cached_size = None

    def get_size(self) -> int:
        if self._cached_size is None:
            self._cached_size = sum(l.get_size() for l in self._nodes)
        return self._cached_size

    @property
    def sub_directories(self):
        return [d for d in self._nodes if isinstance(d, Directory)]

    def __repr__(self):
        return f"<Dir {self.name}, size {self.get_size()}>"


class File(FSNode):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"<File {self.name}, size {self.get_size()}>"


@functools.cache
def build_directory(file_name: str) -> Directory:
    with open(f"./inputs/{file_name}.txt") as f:
        lines = [l.strip() for l in f]

    root_dir = Directory("/", None)
    current_dir = root_dir
    while lines:
        line = lines.pop(0)

        if line.startswith("$ cd"):
            dir = line.split(" ")[-1]
            if dir == "/":
                current_dir = root_dir
            elif dir == "..":
                current_dir = current_dir.parent
            else:
                current_dir = [d for d in current_dir.sub_directories if d.name == dir][0]
        elif line.startswith("$ ls"):
            while lines and not lines[0].startswith("$"):
                p1, p2 = lines.pop(0).split(" ")

                if p1 == "dir":
                    node = Directory(p2, current_dir)
                else:
                    node = File(p2, int(p1))
                current_dir.add_node(node)
    return root_dir


def find_smol_directories(directory: Directory, threshold: int) -> List[Directory]:
    smol_directories = [d for d in directory.sub_directories if d.get_size() <= threshold]
    for d in directory.sub_directories:
        smol_directories += find_smol_directories(d, threshold)
    return smol_directories


def get_all_directories(root_dir: Directory) -> List[Directory]:
    all_dirs = []
    to_expand = [root_dir]
    while to_expand:
        d = to_expand.pop()
        all_dirs.append(d)
        to_expand += d.sub_directories
    return all_dirs


def part_1(file_name: str) -> int:
    return sum(d.get_size() for d in find_smol_directories(build_directory(file_name), 100000))


def part_2(file_name: str) -> int:
    root_dir = build_directory(file_name)
    unused_space = 70000000 - root_dir.get_size()
    dir_size_to_delete = 30000000 - unused_space
    all_dirs = sorted(get_all_directories(build_directory(file_name)), key=lambda d: d.get_size())
    for d in all_dirs:
        if d.get_size() >= dir_size_to_delete:
            return d.get_size()


for file_name in ["test", "real"]:
    print(f"Part 1: {part_1(file_name)}")
    print(f"Part 2: {part_2(file_name)}")
