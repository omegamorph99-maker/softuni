characters = input().split(', ')

ascii = {character: ord(character) for character in characters }

print(ascii)