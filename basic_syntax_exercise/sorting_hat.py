mistake = True
while True:
    name = str(input())

    if name == 'Welcome!':
        break
    elif name == 'Voldemort':
        mistake = False
        print('You must not speak of that name!')
        break

    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6:
        print(f'{name} goes to Hufflepuff.')


if mistake:
    print('Welcome to Hogwarts.')