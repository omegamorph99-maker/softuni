deck_of_cards = input().split(', ')
number_of_lines = int(input())

for number in range(number_of_lines):
    command = input().split(', ')
    initial_command = command[0]
    if initial_command == "Add":
        card_name = command[1]
        if card_name not in deck_of_cards:
            deck_of_cards.append(card_name)
            print('Card successfully added')
        else:
            print('Card is already in the deck')

    elif initial_command == "Remove":
        card_name = command[1]
        if card_name not in deck_of_cards:
            print('Card not found')
        else:
            deck_of_cards.remove(card_name)
            print('Card successfully removed')

    elif initial_command == "Remove At":
        card_index = int(command[1])
        if card_index not in range(len(deck_of_cards)):
            print('Index out of range')
        else:
            deck_of_cards.pop(card_index)
            print('Card successfully removed')

    elif initial_command == "Insert":
        card_index = int(command[1])
        card_name = command[2]
        if card_index not in range(len(deck_of_cards)):
            print('Index out of range')
        elif card_index in range(len(deck_of_cards)) and card_name in deck_of_cards:
            print('Card is already added')
        else:
            deck_of_cards.insert(card_index, card_name)
            print('Card successfully added')



print(', '.join(deck_of_cards))