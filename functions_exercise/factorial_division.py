def factorial(number_one: int, number_two: int) -> float:
    first_factorial = 1
    second_factorial = 1
    for number in range(1, first_number + 1):
       first_factorial *= number

    for number in range(1, second_number + 1):
       second_factorial *= number

    return (f'{(first_factorial / second_factorial):.2f}')

first_number = int(input())
second_number = int(input())


print(factorial(first_number, second_number))