import re

text = input()
rule = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
list_to_buy = []
total_money_spent = 0

while text != "Purchase":
    match = re.search(rule, text)

    if match:
        item, price, quantity = match.groups()
        list_to_buy.append(item)
        total_money_spent += float(price) * int(quantity)
    text = input()

print('Bought furniture:')
for key in list_to_buy:
    print(key)
print(f'Total money spend: {total_money_spent:.2f}')