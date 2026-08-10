dictionary_of_resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())

    if resource not in dictionary_of_resources:
        dictionary_of_resources[resource] = 0
    dictionary_of_resources[resource] += quantity

for key, value in dictionary_of_resources.items():
    print(f'{key} -> {value}')