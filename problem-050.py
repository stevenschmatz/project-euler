def memoize(f):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = f(n)
        cache[n] = result
        return result
    return wrapper

@memoize
def is_prime(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

primes = [n for n in range(10000) if is_prime(n)]

max_consecutive_primes = 0
max_prime_sum = 0

for start_index in range(len(primes)):
    prime_sum = primes[start_index]
    for end_index in range(start_index + 1, len(primes)):
        prime_sum += primes[end_index]

        if prime_sum > 1_000_000:
            break

        if is_prime(prime_sum) and end_index - start_index + 1 > max_consecutive_primes:
            max_consecutive_primes = end_index - start_index + 1
            max_prime_sum = sum(primes[start_index : end_index + 1])

print(max_prime_sum)
