number_of_people = int(input())
elevator_capacity = int(input())

if number_of_people % elevator_capacity == 0:
    final = number_of_people // elevator_capacity
else:
    final = number_of_people // elevator_capacity + 1

print(final)