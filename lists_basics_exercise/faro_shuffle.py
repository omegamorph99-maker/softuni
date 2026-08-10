deck_of_cards = input().split()
left_half = deck_of_cards[:len(deck_of_cards)//2]
right_half = deck_of_cards[len(deck_of_cards)//2:]
number_of_shuffles = int(input())
current_shuffle = []
final_shuffle = []

for number in range(number_of_shuffles):
    for index in range(len(left_half)):
        current_shuffle.append(left_half[index])
        current_shuffle.append(right_half[index])

    left_half = current_shuffle[:len(current_shuffle) // 2]
    right_half = current_shuffle[len(current_shuffle) // 2:]

    final_shuffle = current_shuffle.copy()
    current_shuffle = []

print(final_shuffle)