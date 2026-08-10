list_of_integers = input().split()
count_of_removed_numbers = int(input())
final_list = []

for number in list_of_integers:
    final_list.append(int(number))

for count in range(count_of_removed_numbers):
    lowest_number = min(final_list)
    final_list.remove(lowest_number)

for integer in range(len(final_list)):
    if integer == len(final_list)-1:
        print(final_list[integer])
    else:
        print(f'{final_list[integer]}, ', end='')