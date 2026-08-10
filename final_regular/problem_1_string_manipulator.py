import re

some_string = input()

command = input()



while command != 'End':
    command = command.split()
    current_command = command[0]

    if current_command == 'Translate':
        char, replacement = command[1], command[2]
        for letter in some_string:
            if letter == char:
                some_string = some_string.replace(letter, replacement)
        print(some_string)
    elif current_command == 'Includes':
        substring = command[1]
        if substring in some_string:
            print('True')
        else:
            print('False')
    elif current_command == 'Start':
        substring = command[1]
        patern = f'^{substring}'
        result = re.findall(patern, some_string)
        if result:
            print('True')
        else:
            print('False')
    elif current_command == 'Lowercase':
        some_string = some_string.lower()
        print(some_string)
    elif current_command == 'FindIndex':
        char = command[1]
        some_string = list(some_string)
        for letter in range(len(some_string))[::-1]:
            if some_string[letter] == char:
                print(letter)
                break
        some_string = ''.join(some_string)
    elif current_command == 'Remove':
        start_index, count = int(command[1]), int(command[2])
        first_part = some_string[:start_index]
        second_part = some_string[start_index:start_index+count]
        third_part = some_string[start_index+count:]
        some_string = first_part + third_part
        print(some_string)


    command = input()