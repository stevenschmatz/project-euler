import numpy as np


def parse_file(path='/path/to/p081_matrix.txt'):
    f = open(path)
    num_strings = [line.strip('\n').split(',') for line in f.readlines()]
    return np.array([list(map(int, line)) for line in num_strings])


def flatten(arr):
    return [i for sublist in arr for i in sublist]


def generate_diagonal_iteration_indices(size):
    """Return the indices used to iterate from the bottom
    right corner of a matrix to the top left in rows extending
    from the bottom right corner

    Example:
    |0, 1|  <- matrix of size 2
    |2, 3|

    >>> generate_diagonal_iteration_indices(2)
    [(1, 1), (0, 1), (1, 0), (0, 0)]
    """

    result = []

    for index in range(size - 1, -1, -1):
        indices = range(index, size)
        result.append(list(zip(indices, reversed(indices))))

    for index in range(size - 2, -1, -1):
        indices = range(index, -1, -1)
        result.append(list(zip(indices, reversed(indices))))

    return flatten(result)


def find_minimum_distance_matrix(matrix):
    size = len(matrix)
    distance_matrix = np.zeros(matrix.shape)

    print(generate_diagonal_iteration_indices(size)[:10])
    for x, y in generate_diagonal_iteration_indices(size):
        distance = matrix[x, y]

        if x == size - 1 and y == size - 1:
            distance += 0
        elif x == size - 1:
            distance += distance_matrix[x, y+1]
        elif y == size - 1:
            distance += distance_matrix[x+1, y]
        else:
            distance += min(distance_matrix[x+1, y], distance_matrix[x, y+1])

        distance_matrix[x, y] = distance

    return distance_matrix


def main():
    matrix = parse_file()
    min_dist_matrix = np.zeros(matrix.shape)
    distance_matrix = find_minimum_distance_matrix(matrix)

    print(distance_matrix[0, 0])


if __name__ == "__main__":
    main()

