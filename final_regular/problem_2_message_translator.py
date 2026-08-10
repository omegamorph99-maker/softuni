import re

count_of_string = int(input())
command_check = r'^![A-Z][a-z]{3,}!'
message_check = r'^\[[A-Za-z]{8,}\]$'

while count_of_string > 0:
    count_of_string -= 1
    password = input().split(':')
    ASCII_numbers = []

    command = re.findall(command_check, password[0])
    message = re.findall(message_check, password[1])

    if command and message:
        current_command = ''
        for char in command[0]:
            if char != '!':
                current_command += char

        for letter in message[0]:
            if letter != '[' and letter != ']':
                number = ord(letter)
                ASCII_numbers.append(str(number))
        print(f'{current_command}: {' '.join(ASCII_numbers)}')
    else:
        print('The message is invalid')

