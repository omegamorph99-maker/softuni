products = {}

while True:
    product = input().split(': ')

    if product[0] == 'statistics':
        break

    if product[0] in products:
        products[product[0]] += int(product[1])
    else:
        products.update({product[0]: int(product[1])})

print('Products in stock:')
for key, value in products.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')