text = input()
new_text = ''

for letter in text:
    number = ord(letter) + 3
    new_text += chr(number)

print(new_text)