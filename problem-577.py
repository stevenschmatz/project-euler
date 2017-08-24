from math import ceil


def sum_1_to_n(n: int) -> int:
    return n * (n + 1) // 2


def num_hex_tiles(n: int, hexagon_size: int) -> int:
    """Returns the number of regular hexagons of a given size that can fit into a triangular
    lattice of size n"""

    # An enclosing triangle side length must be at least 3 times as long as an enclosed hexagon
    if n < 3*hexagon_size:
        return 0
    else:
        # Rotation: for a given hexagon of length n, (n - 1) other hexagons can be inscribed inside by choosing
        #     a point in the middle of the hexagon side.
        # Translation: for a given triangle, each additional triangle size increase adds an additional (n + 1)
        #     valid hexagons. Hence, the sum of 1 to n is used.
        return hexagon_size * sum_1_to_n(n - 3*hexagon_size + 1)


def num_all_hex_tiles(n: int) -> int:
    """Returns the number of all regular hexagons that can fit into a triangular lattice
    of size n"""

    # The upper bound for the max hexagon size (inclusive) is the triangle
    # size divided by 3.
    return sum([num_hex_tiles(n, i) for i in range(1, n // 3 + 1)])


def main():
    print(sum([num_all_hex_tiles(n) for n in range(3, 12346)]))


if __name__ == "__main__":
    main()
