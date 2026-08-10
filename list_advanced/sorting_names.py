list_of_names = input().split(', ')

list_of_names = sorted(list_of_names, key=lambda x: (-len(x), x))

print(list_of_names)
