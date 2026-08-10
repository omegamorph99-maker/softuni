number_of_lines = int(input())
magic_word = input()

full_list = []
magic_list=[]

for line in range(number_of_lines):
    string = input()
    full_list.append(string)
    if magic_word in string:
        magic_list.append(string)

print(full_list)
print(magic_list)