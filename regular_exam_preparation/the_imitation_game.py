encrypted_message = input()

command = input()

while command != 'Decode':
    command = command.split('|')
    initial_command = command[0]
    if initial_command == 'Move':
        index = int(command[1])
        left_part = encrypted_message[:index]
        right_part = encrypted_message[index:]
        encrypted_message = right_part + left_part
    elif initial_command == 'Insert':
        index = int(command[1])
        value = command[2]
        left_part = encrypted_message[:index]
        right_part = encrypted_message[index:]
        encrypted_message = left_part + value + right_part
    elif initial_command == 'ChangeAll':
        substring = command[1]
        replace = command[2]
        encrypted_message = encrypted_message.replace(substring, replace)

    command = input()

print(f"The decrypted message is: {encrypted_message}")