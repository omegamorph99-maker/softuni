list_of_numbers = [int(number) for number in input().split(', ')]
positive_numbers = [num for num in list_of_numbers if num >= 0]
negative_numbers = [num for num in list_of_numbers if num < 0]
even_numbers = [num for num in list_of_numbers if num % 2 == 0]
odd_numbers = [num for num in list_of_numbers if num % 2 != 0]

print(f'Positive: {", ".join(map(str,positive_numbers))}')
print(f'Negative: {", ".join(map(str,negative_numbers))}')
print(f'Even: {", ".join(map(str,even_numbers))}')
print(f'Odd: {", ".join(map(str,odd_numbers))}')