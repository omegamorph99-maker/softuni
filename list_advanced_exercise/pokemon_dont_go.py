list_of_pokemon = [int(number) for number in input().split()]

sum_of_removed_elements = 0

while list_of_pokemon:
    index = int(input())


    if index < 0:
        removed_pokemon = list_of_pokemon[0]
        list_of_pokemon[0] = list_of_pokemon[-1]
    elif index >= len(list_of_pokemon):
        list_of_pokemon[-1] = list_of_pokemon[0]
        removed_pokemon = list_of_pokemon[-1]
    else:
        removed_pokemon = list_of_pokemon[index]
        list_of_pokemon.pop(index)

    sum_of_removed_elements += removed_pokemon

    for index in range(len(list_of_pokemon)):
        if list_of_pokemon[index] <= removed_pokemon:
            list_of_pokemon[index] += removed_pokemon
        else:
            list_of_pokemon[index] -= removed_pokemon

print(sum_of_removed_elements)