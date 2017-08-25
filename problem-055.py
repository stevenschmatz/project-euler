def gen_palindromes(limit=10000):
    max_digits = len(str(limit - 1))
    for i in range(10 ** (max_digits // 2)):
        yield int(f'{str(i)}{"".join(list(reversed(str(i))))}')


def is_lychrel(n: int) -> bool:
    def lychrel_iteration(n):
        return int(''.join(list(reversed(str(n))))) + n

    def is_palindrome(n):
        return ''.join(reversed(str(n))) == str(n)

    for i in range(50):
        n = lychrel_iteration(n)
        if is_palindrome(n):
            return False
    else:
        return True


def main():
    print(sum([is_lychrel(i) for i in range(10000)]))


if __name__ == "__main__":
    main()
