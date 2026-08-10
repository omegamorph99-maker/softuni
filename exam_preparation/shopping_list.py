shopping_list = input().split('!')
initial_command = input()

while initial_command != 'Go Shopping!':
    initial_command = initial_command.split()
    command = initial_command[0]
    item = initial_command[1]

    if command == 'Urgent' and item not in shopping_list:
        shopping_list.insert(0,item)

    elif command == 'Unnecessary' and item in shopping_list:
        shopping_list.remove(item)

    elif command == 'Correct' and item in shopping_list:
        index = shopping_list.index(item)
        shopping_list[index] = initial_command[2]

    elif command == 'Rearrange' and item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)

    initial_command = input()

print(', '.join(shopping_list))
