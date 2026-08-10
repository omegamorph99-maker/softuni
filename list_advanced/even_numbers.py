even_numbers = list(map(int, input().split(', ')))

index_of_even_numbers = list(index for index in range(len(even_numbers)) if even_numbers[index] % 2 == 0)

print(index_of_even_numbers)