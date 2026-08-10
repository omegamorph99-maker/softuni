single_string = input().split(', ')
empty_string = []
for number in single_string:
    empty_string.append(int(number))
for number in single_string:
    if number == '0':
        empty_string.remove(int(number))
        empty_string.append(int(number))

print(single_string)