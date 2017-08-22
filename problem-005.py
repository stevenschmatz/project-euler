from functools import reduce
from fractions import gcd

def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

print(reduce(lcm, range(2, 21)))
