text = input()
new_text = ''
explosion = 0

for index in range(len(text)):

    if explosion > 0 and text[index] != '>':
        explosion -=1
        continue

    new_text += text[index]
    if text[index] == '>':
        explosion += int(text[index+1])


print(new_text)
