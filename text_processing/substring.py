remove = input()
whole_string = input()

while remove in whole_string:
    whole_string = whole_string.replace(remove, '')

print(whole_string)