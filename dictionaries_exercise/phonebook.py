phonebook = {}

while True:
    name_and_phone = input().split('-')
    if name_and_phone[0].isdigit():
        break

    name = name_and_phone[0]
    phone = name_and_phone[1]

    phonebook[name] = phone

line = 0
while line < int(name_and_phone[0]):
    line +=1
    check_name = input()
    if check_name not in phonebook:
        print(f'Contact {check_name} does not exist.')
    else:
        print(f'{check_name} -> {phonebook[check_name]}')