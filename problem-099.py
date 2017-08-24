from math import log
from typing import List

FILE_PATH = '/path/to/p099_base_exp.txt'


def parse_file() -> List:
    with open(file_path) as f:
        lines = f.readlines()

    nums_as_str = [line.strip('\n').split(',') for line in lines]
    return [(int(a), int(b)) for a, b in [line for line in nums_as_str]]


def main():
    pairs = parse_file()

    log_transform = [b * log(a) for a, b in pairs]
    maximum_value = max(enumerate(log_transform), key=lambda x: x[1])

    # Lines are 1-indexed
    max_line = maximum_value[0] + 1
    print(max_line)


if __name__ == "__main__":
    main()
