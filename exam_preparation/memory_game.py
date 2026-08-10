sequence_of_elements = input().split()
string_with_int = input()

number_of_turns = 0

while sequence_of_elements:

    if string_with_int == 'end':
        break

    number_of_turns += 1
    string_with_int = string_with_int.split()
    first_index = int(string_with_int[0])
    second_index = int(string_with_int[1])

    if first_index == second_index or first_index not in range(len(sequence_of_elements)) or second_index not in range(len(sequence_of_elements)):
        first_half = sequence_of_elements[:len(sequence_of_elements)//2]
        second_half = sequence_of_elements[len(sequence_of_elements)//2:]

        first_half.append(f'-{str(number_of_turns)}a')
        second_half.insert(0, f'-{str(number_of_turns)}a')

        sequence_of_elements = first_half + second_half
        print('Invalid input! Adding additional elements to the board')

    elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        guessed_number = sequence_of_elements[first_index]
        print(f'Congrats! You have found matching elements - {guessed_number}!')

        sequence_of_elements.remove(guessed_number)
        sequence_of_elements.remove(guessed_number)

    else:
        print('Try again!')

    string_with_int = input()


if len(sequence_of_elements) == 0:
    print(f'You have won in {number_of_turns} turns!')
else:
    print(f'Sorry you lose :(')
    print(' '.join(sequence_of_elements))