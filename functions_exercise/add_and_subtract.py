def sum_numbers(first:int, second:int) -> int:
    sum_of_two = first + second
    return int(sum_of_two)

def subtract(sum_of_two:int, third:int) -> int:
    subtract_of_two = sum_of_two - third
    return subtract_of_two

def add_and_subtract(first:int, second:int, third:int) -> int:
    sum_of_numbers = sum_numbers(first, second)
    subtract_of_numbers = subtract(sum_of_numbers, third)
    return subtract_of_numbers

first_number = int(input())
second_number = int(input())
third_number = int(input())
final_result = add_and_subtract(first_number, second_number, third_number)

print(final_result)