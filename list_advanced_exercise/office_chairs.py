number_of_rooms = int(input())

empty_chairs = 0

for room in range(number_of_rooms):
    room +=1
    chairs, number_of_visitors = input().split()
    chairs = len(chairs)
    number_of_visitors = int(number_of_visitors)
    if chairs - number_of_visitors < 0:
        print(f"{abs(chairs - number_of_visitors)} more chairs needed in room {room}")

    empty_chairs += chairs - number_of_visitors

if empty_chairs >= 0:
    print(f"Game On, {empty_chairs} free chairs left")