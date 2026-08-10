number_of_lines = int(input())
numbers = []

for line in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()
command_list = []

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            command_list.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            command_list.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            command_list.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            command_list.append(number)

print(command_list)