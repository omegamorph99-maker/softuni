
ornament_set = 2
ornament_set_point = 5
tree_skirt = 5
tree_skirt_points = 3
tree_garland = 3
tree_garland_points = 10
tree_lights = 15
tree_lights_points = 17

total_cost = 0
total_points = 0
day = 0

quantity_of_decorations = int(input())
days_until_christmas = int(input())

while days_until_christmas > 0:
    days_until_christmas -= 1
    day += 1

    if day % 11 == 0:
        quantity_of_decorations += 2


    if day % 2 == 0:
        total_cost += ornament_set * quantity_of_decorations
        total_points += ornament_set_point

    if day % 3 == 0:
        total_cost += (tree_skirt * quantity_of_decorations + tree_garland * quantity_of_decorations)
        total_points += (tree_skirt_points + tree_garland_points)

    if day % 5 == 0:
        total_cost += (tree_lights * quantity_of_decorations)
        total_points += tree_lights_points
        if day % 3 == 0:
            total_points += 30


    if day % 10 == 0:
        total_cost += (tree_skirt + tree_garland + tree_lights)
        total_points -= 20



if day % 10 == 0:
    total_points -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_points}')