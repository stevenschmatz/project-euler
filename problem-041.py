from typing import List
from itertools import permutations


def gen_candidates(digits=10) -> List[int]:
    for permutation in permutations(range(digits - 1, 0, -1)):
        if permutation[-1] in [2, 4, 5]:
            continue
        yield int(''.join(map(str, permutation)))


def is_prime(n: int) -> bool:
    return not (n < 2 or any(n % x == 0 for x in range(2, int(n ** 0.5) + 1)))


def main():
    for digits in range(10, 1, -1):
        for candidate in gen_candidates(digits):
            if is_prime(candidate):
                print(candidate)
                return


if __name__ == "__main__":
    main()
