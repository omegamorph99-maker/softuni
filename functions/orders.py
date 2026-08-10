def recipe(order, quantity):
    return{
        'coffee': quantity * 1.50,
        'water': quantity * 1.00,
        'coke': quantity * 1.40,
        'snacks': quantity * 2.00,
    }.get(order,'Invalid order')

ordered_article = str(input())
quantity = int(input())

print(f'{recipe(ordered_article, quantity):.2f}')