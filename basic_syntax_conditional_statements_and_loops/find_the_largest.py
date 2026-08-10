number = int(input())
final_number = []
final_string = ''

while number != 0:
    current_number = number % 10
    number = number // 10
    final_number.append(current_number)

final_number.sort(reverse=True)

for character in final_number:
    final_string += str(character)

print(final_string)