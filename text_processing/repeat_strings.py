sequence_of_strings = input().split()
new_string = ''

for word in sequence_of_strings:
    new_string += word * len(word)

print(new_string)