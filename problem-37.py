def memoize_int(f):
    cache = {}
    def func(n: int):
        if n in cache:
            return cache[n]
        return f(n)
    return func


@memoize_int
def is_prime(n: int) -> bool:
    return n > 1 and all(n % i for i in range(2, n))


def is_right_truncatable_prime(n: int) -> bool:
    s = str(n)
    return all([is_prime(int(s[:i])) for i in range(1, len(s))])


def left_extend_primes(prev_level_primes):
    candidates = [int(f'{i}{p}') for p in prev_level_primes for i in range(10)]
    return list(filter(is_prime, candidates))


def main():
    solution = set()
    prev_level_primes = [3, 5, 7]
    while True:
        candidates = left_extend_primes(prev_level_primes)
        for candidate in candidates:
            if is_right_truncatable_prime(candidate) and candidate > 9 and candidate not in solution:
                solution.add(candidate)
                print(sorted(solution))
                if len(solution) == 11:
                    print(sum(solution))
                    return
        prev_level_primes = candidates


if __name__ == "__main__":
    main()
