def minimal_number(number:list) ->int:
    return min(number)

def maximum_number(number:list) ->int:
    return max(number)

def sum_number(number:list) ->int:
    return sum(number)

sequence_of_numbers = input().split()
sequence_of_numbers_as_int = []

for number in sequence_of_numbers:
    sequence_of_numbers_as_int.append(int(number))

print(f'The minimum number is {minimal_number(sequence_of_numbers_as_int)}')
print(f'The maximum number is {maximum_number(sequence_of_numbers_as_int)}')
print(f'The sum number is: {sum_number(sequence_of_numbers_as_int)}')