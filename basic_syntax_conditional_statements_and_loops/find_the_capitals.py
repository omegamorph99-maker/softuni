word = input()
final_list = []
counter = 0

for character in word:
    if character.isupper():
        final_list.append(counter)

    counter += 1

print(final_list)