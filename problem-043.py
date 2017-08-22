from typing import List
from itertools import permutations
from collections import defaultdict

divisors = [2, 3, 5, 7, 11, 13, 17]


def gen_multiples(limit=1000) -> defaultdict:
    multiples = defaultdict(set)

    for n in divisors:
        for multiple in range(n, limit, n):
            multiples[n].add(multiple)

    return multiples


def all_unique_digits(n: int) -> bool:
    return len(set(str(n))) == len(str(n))


def is_valid_extension(i: str, c: str, multiples: List[int]) -> bool:
    return i not in c and int(f'{i}{c[:2]}') in multiples


def main():
    multiples = gen_multiples()
    candidates = [f'{m:03}' for m in multiples[17] if all_unique_digits(m)]

    for divisor in list(reversed(divisors))[1:]:
        candidates = [f'{i}{c}' for c in candidates for i in map(str, range(10)) if is_valid_extension(i, c, multiples[divisor])]

    result = 0
    for number_str in candidates:
        missing_number = list(set(map(str, range(10))) - set(number_str))[0]
        result += int(f'{missing_number}{number_str}')

    print(result)


if __name__ == "__main__":
    main()
