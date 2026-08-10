empty_list = [0] * 10

while True:
    priority = input().split('-')

    if priority[0] == 'End':
        break

    index = int(priority[0])
    empty_list[index-1] = priority[1]

empty_list = list(ch for ch in empty_list if ch != 0)
print(empty_list)