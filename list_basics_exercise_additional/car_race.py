sequence_of_numbers = input().split()

left_time = 0
right_time = 0

for left in sequence_of_numbers[:len(sequence_of_numbers)//2]:
    if left == '0':
        left_time *= 0.8
    else:
        left_time += int(left)

for right in sequence_of_numbers[:len(sequence_of_numbers)//2:-1]:
    if right == '0':
        right_time *= 0.8
    else:
        right_time += int(right)

if left_time < right_time:
    print(f'The winner is left with total time: {left_time:.2f}')
else:
    print(f'The winner is right with total time: {right_time:.2f}')