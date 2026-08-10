single_string = input().split()
inverted_string = []
for number in (single_string):
    number = int(number) * -1
    inverted_string.append(number)

print(inverted_string)