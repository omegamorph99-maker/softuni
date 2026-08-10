stock_list = input().split()
products = input().split()

stock_list_as_dictionary = {}

for stock in range(0, len(stock_list), 2):
    key = stock_list[stock]
    value = int(stock_list[stock + 1])
    stock_list_as_dictionary[key] = value

for product in products:
    if product not in stock_list_as_dictionary:
        print(f'Sorry, we don\'t have {product}')
    else:
        print(f'We have {stock_list_as_dictionary[product]} of {product} left')