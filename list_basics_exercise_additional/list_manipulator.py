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
            left_side = starting_list[:index+1]
            right_side = starting_list[index+1:]
            starting_list = right_side + left_side
        else:
            print('Invalid index')


    elif initial_command == 'max':
        even_odd = command[1]
        if even_odd == 'even':
            for even in starting_list:
                if even % 2 == 0:
                    even_list.append(even)
            if len(even_list) == 0:
                print('No matches')
            else:
                index = starting_list.index(max(even_list))
                print(index)
        elif even_odd == 'odd':
            for odd in starting_list:
                if odd % 2 == 1:
                    odd_list.append(odd)
            if len(odd_list) == 0:
                print('No matches')
            else:
                index = starting_list.index(max(odd_list))
                print(index)


    elif initial_command == 'min':
        even_odd = command[1]
        if even_odd == 'even':
            for even in starting_list:
                if even % 2 == 0:
                    even_list.append(even)
            if len(even_list) == 0:
                print('No matches')
            else:
                index = starting_list.index(min(even_list))
                print(index)
        elif even_odd == 'odd':
            for odd in starting_list:
                if odd % 2 == 1:
                    odd_list.append(odd)
            if len(odd_list) == 0:
                print('No matches')
            else:
                index = starting_list.index(min(odd_list))
                print(index)


    elif initial_command == 'first':
        count = int(command[1])
        even_odd = command[2]
        if count > len(starting_list):
            print('Invalid count')
        else:
            if even_odd == 'even':
                for even in starting_list:
                    if even % 2 == 0:
                        first_count.append(even)
                        if len(first_count) == count:
                            print(first_count)
                            break
                if len(first_count) == 0 or len(first_count) < count:
                    print(first_count)
            elif even_odd == 'odd':
                for even in starting_list:
                    if even % 2 == 1:
                        first_count.append(even)
                        if len(first_count) == count:
                            print(first_count)
                            break
                if len(first_count) == 0 or len(first_count) < count:
                    print(first_count)


    elif initial_command == 'last':
        count = int(command[1])
        even_odd = command[2]
        if count > len(starting_list):
            print('Invalid count')
        else:
            if even_odd == 'even':
                for even in reversed(starting_list):
                    if even % 2 == 0:
                        first_count.append(even)
                        if len(first_count) == count:
                            print(list(reversed(first_count)))
                            break
                if len(first_count) == 0 or len(first_count) < count:
                    print(list(reversed(first_count)))
            elif even_odd == 'odd':
                for even in reversed(starting_list):
                    if even % 2 == 1:
                        first_count.append(even)
                        if len(first_count) == count:
                            print(list(reversed(first_count)))
                            break
                if len(first_count) == 0 or len(first_count) < count:
                    print(list(reversed(first_count)))

    command = input()


print(starting_list)