number_list = input().split()
absolute_list = []

for number in number_list:
    number = float(number)
    absolute_list.append(abs(number))

print(absolute_list)