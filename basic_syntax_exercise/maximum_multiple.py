divisor = int(input())
boundry = int(input())

for number in range(boundry, divisor -1, -1):
    if number % divisor== 0:
        break

print(number)