money_of_beggars = input().split(', ')
number_of_beggars = int(input())
money_of_beggars_integer = []

for money in money_of_beggars:
    money_of_beggars_integer.append(int(money))

current_beggar_sum = []
start_index = 0
for beggar in range(number_of_beggars):
    current_beggar_money = 0
    for index in range(start_index, len(money_of_beggars_integer), number_of_beggars):
        current_beggar_money += money_of_beggars_integer[index]

    current_beggar_sum.append(current_beggar_money)
    start_index += 1

print(current_beggar_sum)