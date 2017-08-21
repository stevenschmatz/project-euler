result = 0
last_two = [1, 2]

while last_two[1] < 4_000_000:
    if last_two[1] % 2 == 0:
        result += last_two[1]
    last_two = [last_two[1], sum(last_two)]

print(result)
