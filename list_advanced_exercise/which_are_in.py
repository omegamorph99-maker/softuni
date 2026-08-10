first_string = input().split(', ')
second_string = input().split(', ')
new_list = []

for char in first_string:
    for word in second_string:
        if char in word and char not in new_list:
            new_list.append(char)

print(new_list)