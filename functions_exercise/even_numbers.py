def even_numbers(numbers:int) -> bool:
    if numbers % 2 == 0:
        return True
    else:
        return False

some_numbers = input().split()
some_number_as_int = []
for number in some_numbers:
    some_number_as_int.append(int(number))

result = filter(even_numbers, some_number_as_int)
print(list(result))