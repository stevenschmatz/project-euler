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


def digit_factorial(n):
    return sum([factorial(int(i)) for i in str(n)])


def cycle_length(n):
    found = set([n])
    transformed = None

    while transformed is None or transformed not in found:
        if transformed is not None:
            found.add(transformed)
        transformed = digit_factorial(transformed if transformed is not None else n)

    return len(found)


def main():
    print(sum([cycle_length(i) == 60 for i in range(1, 1_000_000)]))


if __name__ == "__main__":
    main()
