gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    gift = command[1]
    if command[0] == 'OutOfStock':
        for toy in gifts:
            if toy == gift:
                index = gifts.index(toy)
                gifts[index] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if index in range(len(gifts)):
            gifts[index] = gift
    elif command[0] == 'JustInCase':
        gifts[-1] = gift

    command = input()

gifts = [gift for gift in gifts if gift != 'None']

print(' '.join(gifts))