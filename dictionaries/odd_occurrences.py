elements = input().split()
all_elements = {}

for element in elements:
    element_lower = element.lower()
    if element_lower not in all_elements:
        all_elements[element_lower] = 0
    all_elements[element_lower] += 1

for key, value in all_elements.items():
    if value % 2 != 0:
        print(key, end=' ')