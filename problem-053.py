def memoize(f):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        return f(n)
    return wrapper


@memoize
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def main():
    print(sum([combination(n, r) > 1_000_000 for n in range(1, 101) for r in range(1, n + 1)]))


if __name__ == "__main__":
    main()
