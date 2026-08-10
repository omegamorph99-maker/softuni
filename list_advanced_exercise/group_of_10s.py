group_of_numbers = [int(number) for number in input().split(',')]

group = 0

while group_of_numbers:
    group += 10
    current_group =[]
    for number in group_of_numbers:
        if number <= group:
            current_group.append(number)

    group_of_numbers = [char for char in group_of_numbers if char not in current_group]
    print(f"Group of {group}'s: {current_group}")