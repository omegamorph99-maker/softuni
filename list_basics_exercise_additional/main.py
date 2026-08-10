starting_list = [int(number) for number in input().split()]
command = input()


while command != 'end':

    even_list = []
    odd_list = []
    first_count = []

    command = command.split()
    initial_command = command[0]
    if initial_command == 'exchange':
        index = int(command[1])
        if index < len(starting_list):
            left_side = starting_list[:index]
            right_side = starting_list[index:]
            starting_list = right_side + left_side
        else:
            print('Invalid index')

print(starting_list)