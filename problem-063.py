def is_powerful(base, exp):
    return 10 ** (exp-1) <= base**exp and base**exp < 10 ** exp

print(sum([sum(map(lambda i: is_powerful(n, i), range(1000))) for n in range(1, 100)]))
