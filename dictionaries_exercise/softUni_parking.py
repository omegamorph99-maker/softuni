parking_log = {}
number_of_lines = int(input())
line = 0

while line < number_of_lines:
    line +=1
    command = input().split()

    if command[0] == "register":
        username, plate_number = command[1], command[2]
        if username not in parking_log.keys():
            parking_log[username] = plate_number
            print(f'{username} registered {plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking_log[username]}')
    elif command[0] == "unregister":
        username = command[1]
        if username not in parking_log.keys():
            print(f'ERROR: user {username} not found')
        else:
            del parking_log[username]
            print(f'{username} unregistered successfully')


for key, value in parking_log.items():
    print(f'{key} => {value}')