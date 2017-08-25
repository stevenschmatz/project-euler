from typing import List
from math import ceil, sqrt


def gen_diagonals():
    layer_num = 1
    while True:
        square = (1 + 2*layer_num) ** 2
        for i in range(4):
            yield square - 2*i*layer_num
        layer_num += 1


def is_prime(n: int) -> bool:
    """This implementation is faster than standard trial division."""

    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i <= ceil(sqrt(n)):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def compute_mean(old_mean: float, old_count: int, new_elements: List[int]) -> float:
    new_count = old_count + len(new_elements)
    new_mean = sum(new_elements) / len(new_elements)

    return old_mean + (len(new_elements) / new_count) * (new_mean - old_mean)


def main():
    diagonal_generator = gen_diagonals()

    # 1 is not prime
    mean = 0.0
    num_elements = 1
    side_length = 1

    while mean > 0.1 or mean == 0.0:
        new_diag_elements = [next(diagonal_generator) for _ in range(4)]
        primes = [is_prime(element) for element in new_diag_elements]
        mean = compute_mean(mean, num_elements, primes)
        num_elements += 4
        side_length += 2

    print(side_length)


if __name__ == "__main__":
    main()
