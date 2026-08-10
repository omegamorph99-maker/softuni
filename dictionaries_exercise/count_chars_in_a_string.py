characters = input()
count_of_characters = {}

for character in characters:
    if  character == ' ':
        continue
    if character not in count_of_characters:
        count_of_characters[character] = 0
    count_of_characters[character] += 1

for key, value in count_of_characters.items():
    print(f'{key} -> {value}')