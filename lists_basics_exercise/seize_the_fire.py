fire_and_level = input().split('#')
amount_of_water = int(input())

HIGH_LEVEL = range(81, 125+1)
MEDIUM_LEVEL = range(51, 80+1)
LOW_LEVEL = range(1, 50+1)
effort = 0
total_fire = 0
extinguished_cells = []

for cells in fire_and_level:
    cell = cells.split(' = ')
    fire_intensity, fire_level = cell[0], int(cell[1])
    if amount_of_water >= fire_level:
        if fire_intensity == 'High' and fire_level in HIGH_LEVEL:
            amount_of_water -= fire_level
            effort += (fire_level * 0.25)
            total_fire += fire_level
            extinguished_cells.append(fire_level)
        elif fire_intensity == 'Medium' and fire_level in MEDIUM_LEVEL:
            amount_of_water -= fire_level
            effort += (fire_level * 0.25)
            total_fire += fire_level
            extinguished_cells.append(fire_level)
        elif fire_intensity == 'Low' and fire_level in LOW_LEVEL:
            amount_of_water -= fire_level
            effort += (fire_level * 0.25)
            total_fire += fire_level
            extinguished_cells.append(fire_level)
        else:
            continue

print('Cells:')
for cells in extinguished_cells:
    print(f'- {cells}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
