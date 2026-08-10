initial_energy = 100
initial_coins = 100

events = input().split('|')
event_count = 0

for event in events:
    event = event.split('-')
    current_event, current_number = event[0], int(event[1])
    if current_event == 'rest':
        current_energy = initial_energy
        initial_energy += current_number
        if initial_energy > 100:
            initial_energy = 100
        print(f'You gained {initial_energy - current_energy} energy.')
        print(f'Current energy: {initial_energy}.')
    elif current_event == 'order':
        if initial_energy >= 30:
            initial_coins += current_number
            initial_energy -= 30
            print(f'You earned {current_number} coins.')
        else:
            initial_energy += 50
            print(f'You had to rest!')
            if initial_energy > 100:
                initial_energy = 100
    else:
        if initial_coins >= current_number:
            initial_coins -= current_number
            print(f'You bought {current_event}.')
        else:
            print(f'Closed! Cannot afford {current_event}.')
            break
    event_count += 1

if event_count == len(events):
    print(f'Day completed!')
    print(f'Coins: {initial_coins}')
    print(f'Energy: {initial_energy}')