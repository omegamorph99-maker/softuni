key = int(input())
number_of_lines =  int(input())
word = ''

for line in range(number_of_lines):
    character = input()
    number = ord(character)
    character = chr(number+key)
    word += character

print(word)

