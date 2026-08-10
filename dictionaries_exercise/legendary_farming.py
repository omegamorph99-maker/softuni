items = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False
while True:
    dropped_items = input().split()

    for current_item in range(0,len(dropped_items), 2):
        quantity = int(dropped_items[current_item])
        item = dropped_items[current_item+1].lower()

        if item not in items.keys():
            items[item] = 0
        items[item] += quantity

        for key in items.keys():

            if key == 'shards' and items[key] >= 250:
                items[key] -= 250
                print('Shadowmourne obtained!')
                obtained = True
                break
            elif key == 'fragments' and items[key] >= 250:
                items[key] -= 250
                print('Valanyr obtained!')
                obtained = True
                break
            elif key == 'motes' and items[key] >= 250:
                items[key] -= 250
                print('Dragonwrath obtained!')
                obtained = True
                break

        if obtained:
            break

    if obtained:
        break

for key, value in items.items():
    print(f'{key}: {value}')