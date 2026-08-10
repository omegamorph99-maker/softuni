item_list = input().split('|')
budget = int(input())

clothes = range (1,50)
shoes = range (1,35)
accessories = range (1,21)
train_tickets = 150

safe_budget = budget
profit = 0
list_of_sold_items = []

for items in item_list:
    item = items.split('->')
    product, price = item[0], float(item[1])
    if budget >= price:
        if product == 'Clothes' and  price <=50:
            budget -= price
            profit += price * 1.4
            list_of_sold_items.append(price * 1.4)
        elif product == 'Shoes' and price <= 35:
            budget -= price
            profit += price * 1.4
            list_of_sold_items.append(price * 1.4)
        elif product == 'Accessories' and price <= 20.5:
            budget -= price
            profit += price * 1.4
            list_of_sold_items.append(price * 1.4)

profit += budget

for sold_items in list_of_sold_items:
    print(f'{sold_items:.2f}', end=' ')
print()
print(f"Profit: {(profit - safe_budget):.2f}")
if profit >= train_tickets:
    print("Hello, France!" )
else:
    print("Not enough money.")