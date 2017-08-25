from fractions import Fraction
import sys


def get_continued_fraction(depth=1):
    if depth == 1:
        return 1 + Fraction(1, 2)
    else:
        return 1 + Fraction(1, 1 + get_continued_fraction(depth - 1))


def main():
    # You usually shouldn't set this. However the recursion limit default is 1000.
    # This is only around slightly under what we need to compute a 1000-depth
    # continued fraction, so you can make an exception here.
    sys.setrecursionlimit(1337)

    fractions = [get_continued_fraction(i) for i in range(1, 1001)]

    print(sum([len(str(frac.numerator)) > len(str(frac.denominator)) for frac in fractions]))


if __name__ == "__main__":
    main()
