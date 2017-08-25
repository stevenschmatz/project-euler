def parse_file(path='/Users/schmatz/Desktop/p067_triangle.txt'):
    f = open(path, 'r')
    lines = [line.strip('\n').split(' ') for line in f.readlines()]
    return [list(map(int, line)) for line in lines]

def compute_dist_triangle(triangle):
    dist_triangle = [[num for num in row] for row in triangle]

    dist_triangle[0][0] = triangle[0][0]

    for row_index, row in enumerate(triangle):
        if row_index == len(triangle) - 1:
            break

        for index, num in enumerate(row):
            current_dist = dist_triangle[row_index][index]
            dist_triangle[row_index+1][index] = max(dist_triangle[row_index+1][index], triangle[row_index+1][index] + current_dist)
            dist_triangle[row_index+1][index+1] = max(dist_triangle[row_index+1][index+1], triangle[row_index+1][index+1] + current_dist)

    return dist_triangle


def main():
    triangle = parse_file()
    dist_triangle = compute_dist_triangle(triangle)
    print(max(dist_triangle[-1]))


if __name__ == "__main__":
    main()
