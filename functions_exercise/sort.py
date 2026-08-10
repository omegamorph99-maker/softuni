sequence_of_numbers = input().split()
sequence_of_numbers_as_int = []

for number in sequence_of_numbers:
    sequence_of_numbers_as_int.append(int(number))

sequence_of_numbers_as_int = sorted(sequence_of_numbers_as_int)
print(sequence_of_numbers_as_int)