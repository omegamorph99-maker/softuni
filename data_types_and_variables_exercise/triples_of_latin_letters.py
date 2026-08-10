number = int(input())

for character_1 in range(97, number + 97):

    for character_2 in range(97, number + 97):

        for character_3 in range(97, number + 97):
            print(f'{chr(character_1)}{chr(character_2)}{chr(character_3)}')
