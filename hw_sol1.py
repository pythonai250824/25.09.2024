
numbers: list[int] = []
for i in range(1, 100 + 1):
    numbers.append(i)

print(numbers[0])
print(numbers[99])
print(numbers[len(numbers) - 1])

print(len(numbers))

print(numbers[2: 12])

print(numbers[79:])

print(numbers[:17])

print(numbers[::-1])

print(numbers[1::2])

print(numbers[6::7])

print(numbers[9::10])

print(numbers[98:66 - 3:-3])
print(numbers[-2:66 - 3:-3])

numbers.insert(50, 999)
print(numbers[40:60])

the_100: int = numbers.pop()
print("...", numbers[90:])


