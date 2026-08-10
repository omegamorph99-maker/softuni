def smallest_of_three_numbers(number_1, number_2, number_3):
    return min(number_1, number_2, number_3)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

list_of_numbers = [number_1, number_2, number_3]

print(smallest_of_three_numbers(list_of_numbers[0], list_of_numbers[1], list_of_numbers[2]))