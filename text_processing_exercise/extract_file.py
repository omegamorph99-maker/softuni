path = input()
name = ''

for index in path[::-1]:
    if index == "\\":
        break
    name += index
name = name[::-1]
name = name.split('.')

print(f'File name: {name[0]}')
print(f'File extension: {name[1]}')