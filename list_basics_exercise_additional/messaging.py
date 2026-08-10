sequence_of_numbers = input().split()
string = input()

hidden_message = ''
message = []

for letter in string:
    message.append(letter)

for number in sequence_of_numbers:
    sum_of_characters = 0
    for character in number:
        number = int(number)
        sum_of_characters += number%10
        number = number//10

    if sum_of_characters > len(message) -1:
        sum_of_characters -= len(message)

    hidden_message += message[sum_of_characters]
    del message[sum_of_characters]

print(hidden_message)