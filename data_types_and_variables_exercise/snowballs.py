number_of_snowball = int(input())
max_weigh_of_snowball = 0
max_needed_time = 0
max_quality = 0
max_value = 0

for current_snowball in range(number_of_snowball):
    current_weigh_of_snowball = int(input())
    current_needed_time = int(input())
    current_quality = int(input())
    current_value = (current_weigh_of_snowball // current_needed_time) ** current_quality

    if current_value > max_value:
        max_weigh_of_snowball = current_weigh_of_snowball
        max_needed_time = current_needed_time
        max_quality = current_quality
        max_value = current_value

print(f'{max_weigh_of_snowball} : {max_needed_time} = {max_value} ({max_quality})')