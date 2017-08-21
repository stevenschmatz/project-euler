from typing import List


def gen_palindromes(longest_palindrome_length: int) -> List[int]:
    """Generates all palindromes of longest_palindrome_length in reversed order."""

    one_sided_palindrome_max = 10 ** (longest_palindrome_length // 2)
    palindromes = [int(f'{i}{"".join(reversed(str(i)))}') for i in range(one_sided_palindrome_max)]

    return reversed(sorted(palindromes))


def float_is_int(f: float) -> bool:
    return int(f) == f


def is_three_digit(n: int) -> bool:
    return n >= 100 and n < 1000


def main():
    longest_palindrome_length = len(str(999*999))
    palindromes = gen_palindromes(longest_palindrome_length)

    for palindrome in palindromes:
        for factor_1 in range(100, 1000):
            if palindrome % factor_1 == 0 and is_three_digit(palindrome / factor_1) and float_is_int(palindrome / factor_1):
                print(palindrome)
                return


if __name__ == "__main__":
    main()
