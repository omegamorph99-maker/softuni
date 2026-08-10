water_tank = 255
number_of_lines = int(input())
for lines in range(number_of_lines):
    liters = int(input())
    if (water_tank - liters) < 0:
        print('Insufficient capacity!')
        continue
    water_tank -= liters

print(255 - water_tank)