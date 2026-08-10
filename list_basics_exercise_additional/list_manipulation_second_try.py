starting_list = list((int(number) for number in input().split()))

command = input()

while command != 'end':
    command = command.split()
    initial_command = command[0]

    if initial_command == 'exchange':
        index = int(command[1])
        if abs(index) >= len(starting_list):
            print('Invalid index')
        else:
            left_side = starting_list[:index+1]
            right_side = starting_list[index+1:]
            starting_list = right_side + left_side
    elif initial_command == 'max':
        odd_even = command[1]
        max_number = -9999999999999999999999
        if odd_even == 'even':
            for number in starting_list:
                if number % 2 == 0 and number > max_number:
                    max_number = number
            if max_number == -9999999999999999999999:
                print("No matches")
            else:
                for i in range(len(starting_list) - 1, -1, -1):
                    if starting_list[i] == max_number:
                        print(i)
                        break
        else:
            for number in starting_list:
                if number % 2 != 0 and number > max_number:
                    max_number = number
            if max_number == -9999999999999999999999:
                print("No matches")
            else:
                for i in range(len(starting_list) - 1, -1, -1):
                    if starting_list[i] == max_number:
                        print(i)
                        break
    elif initial_command == 'min':
        odd_even = command[1]
        min_number = 9999999999999999999999
        if odd_even == 'even':
            for number in starting_list:
                if number % 2 == 0 and number < min_number:
                    min_number = number
            if min_number == 9999999999999999999999:
                print("No matches")
            else:
                for i in range(len(starting_list) - 1, -1, -1):
                    if starting_list[i] == min_number:
                        print(i)
                        break
        elif odd_even == 'odd':
            for number in starting_list:
                if number % 2 != 0 and number < min_number:
                    min_number = number
            if min_number == 9999999999999999999999:
                print("No matches")
            else:
                for i in range(len(starting_list) - 1, -1, -1):
                    if starting_list[i] == min_number:
                        print(i)
                        break
    elif initial_command == 'first':
        count = int(command[1])
        even_odd = command[2]
        list_of_num = []
        if len(starting_list) < count:
            print('Invalid count')
        elif even_odd == 'even':
            for number in starting_list:
                if number % 2 == 0:
                    list_of_num.append(number)
                    if len(list_of_num) == count:
                        break
            print(list_of_num)
        elif even_odd == 'odd':
            for number in starting_list:
                if number % 2 != 0:
                    list_of_num.append(number)
                    if len(list_of_num) == count:
                        break
            print(list_of_num)
    elif initial_command == 'last':
        count = int(command[1])
        even_odd = command[2]
        list_of_num = []
        if len(starting_list) < count:
            print('Invalid count')

        elif even_odd == 'even':
            for number in starting_list[::-1]:
                if number % 2 == 0:
                    list_of_num.append(number)
                    if len(list_of_num) == count:
                        break
            list_of_num.reverse()
            print(list_of_num)
        elif even_odd == 'odd':
            for number in starting_list[::-1]:
                 if number % 2 != 0:
                     list_of_num.append(number)
                     if len(list_of_num) == count:
                         break
            list_of_num.reverse()
            print(list_of_num)


    command = input()

print(starting_list)