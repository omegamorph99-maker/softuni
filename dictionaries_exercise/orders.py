product_quantity = {}
product_price = {}

while True:
    product = input().split(' ')

    if product[0] == 'buy':
        break

    current_product, price, quantity = product[0], float(product[1]), float(product[2])

    if current_product not in product_quantity:
        product_quantity[current_product] = 0

    product_quantity[current_product] += quantity
    product_price[current_product] = price


for key in product_quantity:
    print(f'{key} -> {(product_quantity[key] * product_price[key]):.2f}')