def aliquot_sum(num: int) -> bool:
    can_divide = []
    for divider in range(1, num):
        if num % divider == 0:
            can_divide.append(divider)

    if sum(can_divide) == num:
        return True

number = int(input())

if aliquot_sum(number):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')