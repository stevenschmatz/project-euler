from math import sqrt

def pentagonal(n):
    return int(n*(3*n -1) / 2)

def is_pentagonal(x):
    if 24*x + 1 < 0: return False
    n = (sqrt(24*x + 1) + 1) / 6.0
    return int(n) == n


last_pentagonal = pentagonal(2)
differences = [pentagonal(2) - pentagonal(1)]
index = 3

while True:
    next_pentagonal = pentagonal(index)

    differences = [diff + (next_pentagonal - last_pentagonal) for diff in differences]
    differences.append(next_pentagonal - last_pentagonal)

    for index, difference in enumerate(reversed(list(differences))):
        if is_pentagonal(difference):
            p_k = next_pentagonal
            p_j = pentagonal(len(differences) - index - 2)
            if is_pentagonal(p_k + p_j):
                print(p_k - p_j)
                exit()

    last_pentagonal = next_pentagonal
    index += 1
