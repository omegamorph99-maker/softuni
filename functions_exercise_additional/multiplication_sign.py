number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

numbers = [number_1, number_2, number_3]
counter = 0

if number_1 == 0 or number_2 == 0 or number_3 == 0:
    print('zero')
else:
    for number in numbers:
        if number < 0:
            counter +=1

    if counter % 2 == 0:
        print('positive')
    else:
        print('negative')