from typing import List
from itertools import permutations


def gen_primes(limit=10000):
    """Generates all primes up to a given limit."""

    candidates = set(range(2, limit))
    primes = []

    while len(candidates) > 0:
        prime = min(candidates)
        primes.append(prime)
        for number in range(prime, limit, prime):
            candidates.discard(number)

    return primes


def find_prime_permutations(primes, n):
    """Returns all permutations of n if they are prime."""

    candidates = [int("".join(digits)) for digits in sorted(set(permutations(str(n))))]
    return [c for c in candidates if c in primes]


def gen_pairs(l: List[int]):
    def sort_pair(element_1, element_2):
        return ((min(element_1, element_2), max(element_1, element_2)))

    return sorted(set([sort_pair(e_1, e_2) for e_1 in l for e_2 in l if e_1 != e_2]))


def has_duplicates(l):
    return len(set(l)) != len(l)


def find_duplicates(l):
    already_found_elements = set()
    duplicates = []

    for element in l:
        if element in already_found_elements:
            duplicates.append(element)
        already_found_elements.add(element)

    return sorted(duplicates)



four_digit_primes = [prime for prime in gen_primes() if prime >= 1000]
primes_set = set(four_digit_primes)

results = set()

for prime in four_digit_primes:
    prime_permutations = sorted(find_prime_permutations(primes_set, prime))
    prime_pairs = gen_pairs(prime_permutations)
    prime_diffs = [b - a for a, b in prime_pairs]

    if has_duplicates(prime_diffs):
        for difference in find_duplicates(prime_diffs):
            diff_pairs = [pair for pair in prime_pairs if pair[1] - pair[0] == difference]
            for i in range(len(diff_pairs) - 1):
                if diff_pairs[i][1] == diff_pairs[i+1][0]:
                    get_str = lambda i: f'{diff_pairs[i][0]}{diff_pairs[i][1]}'

                    concatenated_num = get_str(i) + get_str(i+1)
                    results.add(concatenated_num)

print(results)
