string = ''

while bool :
    string = input()
    if string == 'End':
        bool = False
        continue

    if string == 'SoftUni':
        continue

    for character in string:
        print(character*2, end= '')
    print()
