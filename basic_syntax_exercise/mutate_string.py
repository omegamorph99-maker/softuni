first_string = input()
second_string = input()

for index in range(len(first_string)):

    left_part = second_string[:index+1]
    right_part = first_string[index+1:]
    if first_string[index] != second_string[index]:
        print(f'{left_part}{right_part}')