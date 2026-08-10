import re

number_of_lines = int(input())
rule = r'^@#+([A-Za-z0-9]+)@#+$'

while number_of_lines > 0:
    barcode = input()

    if not(re.match(rule, barcode)):
        print('Invalid barcode')
        number_of_lines -= 1
        continue

    match = re.match(rule, barcode)
    product = match.group(1)

    if not product[0].isupper():
        print('Invalid barcode')
        number_of_lines -= 1
        continue
    elif len(product) < 6:
        print('Invalid barcode')
        number_of_lines -= 1
        continue
    elif not product[-1].isupper():
        print('Invalid barcode')
        number_of_lines -= 1
        continue

    product_group = ''

    for letter in product:
        if letter.isdigit():
            product_group += letter

    if not product_group:
        product_group = '00'

    print(f"Product group: {product_group}")
    number_of_lines -= 1