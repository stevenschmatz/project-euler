import math

number = 600851475143


def largest_prime_factor(n: int) -> int:
    largest = None
    for i in range(2, math.floor(math.sqrt(n))):
        while n % i == 0:
            n /= i
            largest = i
    return largest or n


print(largest_prime_factor(number))
