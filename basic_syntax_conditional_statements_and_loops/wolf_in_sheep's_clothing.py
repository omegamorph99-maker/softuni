the_animals = input().split(', ')
wolf = True
queued_animal = -1
while True:
    if the_animals[queued_animal] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    elif the_animals[queued_animal-1] == 'wolf':
        print(f'Oi! Sheep number {abs(queued_animal)}! You are about to be eaten by a wolf!')
        break
    else:
        queued_animal -= 1
        continue