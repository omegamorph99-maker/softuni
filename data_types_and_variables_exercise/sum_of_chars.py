number_of_lines = int(input())
sum = 0

for line in range(number_of_lines):
    character = input()
    sum += ord(character)

print(f'The sum equals: {sum}')