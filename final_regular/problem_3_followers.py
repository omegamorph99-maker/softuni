followers = {}

command = input()

while command != "Log out":
    command = command.split(': ')
    current_command = command[0]
    if current_command == 'New follower':
        username = command[1]
        if not username in followers.keys():
            followers[username] = {'likes': 0, 'comments': 0}
    elif current_command == 'Like':
        username, count = command[1], int(command[2])
        if not username in followers.keys():
            followers[username] = {'likes': count, 'comments': 0}
        else:
            followers[username]['likes'] += count
    elif current_command == 'Comment':
        username = command[1]
        if not username in followers.keys():
            followers[username] = {'likes': 0, 'comments': 1}
        else:
            followers[username]['comments'] += 1
    elif current_command == 'Blocked':
        username = command[1]
        if not username in followers.keys():
            print(f'{username} doesn\'t exist.')
        else:
            followers.pop(username)

    command = input()


count_of_followers = len(followers.keys())
print(f'{count_of_followers} followers')

for key, value in followers.items():
    sum_of_activity = int(followers[key]['likes']) + int(followers[key]['comments'])
    print(f'{key}: {sum_of_activity}')