number_of_lines = int(input())

cars = {}

while number_of_lines > 0:
    current_car = input().split("|")
    car, mileage, fuel = current_car[0], int(current_car[1]), int(current_car[2])

    cars[car] = {'mileage': mileage, 'fuel': fuel}
    number_of_lines -= 1

command = input()

while command != 'Stop':
    command = command.split(' : ')
    current_command = command[0]
    if current_command == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]['fuel'] < fuel:
            print('Not enough fuel to make that ride')
        elif cars[car]['fuel'] >= fuel:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

        if cars[car]['mileage'] >= 100000:
            del cars[car]
            print(f'Time to sell the {car}!')

    elif current_command == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        current_fuel = cars[car]['fuel']
        cars[car]['fuel'] += fuel
        if cars[car]['fuel'] > 75:
            cars[car]['fuel'] = 75
            print(f'{car} refueled with {75-current_fuel} liters')
        else:
            print(f'{car} refueled with {fuel} liters')

    elif current_command == 'Revert':
        car = command[1]
        kilometers = int(command[2])
        current_kilometers = int(cars[car]['mileage'])
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

    command = input()


for car, value in cars.items():
    mileage = value['mileage']
    fuel = value['fuel']
    print (f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')