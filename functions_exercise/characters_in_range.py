def list_as_characters(first:str, second:str) -> list:
    characters = []
    for character in range(ord(first)+1, ord(second)):
        characters.append(chr(character))
    return characters

first_character = input()
second_character = input()

print(" ".join(list_as_characters(first_character, second_character)))