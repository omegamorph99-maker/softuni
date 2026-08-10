factor = int(input())
count = int(input())
numbers = []

for number in range(1, count + 1):
    numbers.append(factor * number)

print(numbers)