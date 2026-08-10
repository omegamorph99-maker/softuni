number_of_people = input().split()
execute_indicator = int(input())

number_of_people_as_int = []
order_of_executions = []
counter = 1

for number in number_of_people:
    number_of_people_as_int.append(int(number))

for person in number_of_people_as_int:
    if person % execute_indicator == 0:
        order_of_executions.append(person)
        number_of_people_as_int.remove(person)


print(order_of_executions)