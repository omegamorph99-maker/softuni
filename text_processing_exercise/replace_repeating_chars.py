text = input()
new_text = " "

for letter in text:
    if letter != new_text[-1]:
        new_text += letter

print(new_text.strip())