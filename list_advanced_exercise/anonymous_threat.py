starting_list = input().split()

command = [1]
some_list = []

while command[0] != '3:1':

    helping_list = []
    helping_string = ''
    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])

        if end_index >= len(starting_list):
            end_index = len(starting_list)

        helping_string = ''.join(starting_list[start_index:end_index+1])
        starting_list[start_index:end_index +1] = [helping_string]
            #helping_list = str(''.join(starting_list[int(command[1]):int(command[2])]))

        for word in (starting_list[start_index+1:end_index+2]):
            starting_list.remove(word)



    if command[0] == 'divide':
        index = int(command[1])
        number_of_cuts = int(command[2])

        if number_of_cuts == 0:
            continue
        division_length = len(starting_list[index]) // number_of_cuts
        if division_length == 0:
            continue

        for char in starting_list[index]:
            helping_string += char
            if len(helping_list) < number_of_cuts - 1 and len(helping_string) == division_length:
                helping_list.append(helping_string)
                helping_string = ''

        helping_list.append(helping_string)

        starting_list.pop(index)
        for chr in helping_list[-1::-1]:
            starting_list.insert(index,chr)

    command = input().split()




print(' '.join(starting_list))
