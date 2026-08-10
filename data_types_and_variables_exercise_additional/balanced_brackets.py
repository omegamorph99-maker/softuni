number_of_lines = int(input())
brackets = ''
count_of_open = 0
count_of_close = 0
Balanced = False

for line in range(number_of_lines):
    symbol = input()

    if (symbol == ')' and brackets != '(') or (symbol == '(' and brackets == '('):
        break

    if symbol == '(':
        brackets = '('
        count_of_open += 1

    if brackets == '(' and symbol != ')':
        Balanced = False

    if symbol == ')':
        count_of_close += 1

    if symbol == ')' and brackets == '(' and count_of_open == count_of_close:
        Balanced = True
        brackets = ''

if Balanced:
    print('BALANCED')
else:
    print('UNBALANCED')