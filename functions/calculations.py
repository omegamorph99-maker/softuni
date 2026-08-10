def calculate(operation, number1, number2):
    if operation == 'multiply':
        return number1 * number2
    elif operation == 'divide':
        return number1 // number2
    elif operation == 'add':
        return number1 + number2
    elif operation == 'subtract':
        return number1 - number2

operator = input()
number1 = int(input())
number2 = int(input())

print(calculate(operator, number1, number2))