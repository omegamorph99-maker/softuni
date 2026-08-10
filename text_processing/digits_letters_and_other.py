text = input()

digit = ''
character = ''
others = ''

for char in text:
    if char.isdigit():
        digit += char
    elif char.isalpha():
        character += char
    else:
        others += char

print(digit)
print(character)
print(others)