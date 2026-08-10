def even_sum(some_numbers: list) -> int:
    sum_even = 0
    sum_odd = 0
    for value in some_numbers:
        if value % 2 == 0:
            sum_even += value
        else:
            sum_odd += value
    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


number = input()
number_as_list = []

for character in number:
    number_as_list.append(int(character))


print(even_sum(number_as_list))