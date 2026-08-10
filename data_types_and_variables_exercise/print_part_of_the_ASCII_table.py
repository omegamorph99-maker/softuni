first_number = int(input())
last_number = int(input())

for character in range(first_number, last_number + 1):
    current_character = chr(character)
    print(current_character, end=' ')