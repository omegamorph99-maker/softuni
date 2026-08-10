some_food = input().split()

food_dictionary = {}

for food in range(0, len(some_food), 2):
    key = some_food[food]
    value = int(some_food[food + 1])
    food_dictionary[key] = value


print(food_dictionary)