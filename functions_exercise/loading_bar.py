number = int(input())
percents_count = number // 10

if percents_count == 10:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
elif percents_count == 0:
    print('[..........]')
    print('Still loading...')
else:
    print(f'{number}% [{"%" * percents_count}{"."*(10-percents_count)}]')
    print('Still loading...')