budget = int(input())
final_price = 0
while True:
    expence = input()

    if expence == 'End':
        print('You bought everything needed.')
        break

    new_item = int(expence)

    if final_price + new_item > budget:
        print('You went in overdraft!')
        break

    final_price += new_item