def tribonacci_sequence(some_list: list, numbers_in_list: int) -> list:
    if numbers_in_list == 1:
        some_list = [1]
    elif numbers_in_list == 2:
        some_list = [1, 1]
    elif numbers_in_list >= 3:
        some_list = [1, 1, 2]
        for numbers in range(4, numbers_in_list + 1, +1):

            next_number = some_list[numbers - 2] + some_list[numbers - 3] + some_list[numbers - 4]

            some_list.append(next_number)

    return ' '.join(map(str, some_list))


sequence = []
number = int(input())

print(tribonacci_sequence(sequence, number))
