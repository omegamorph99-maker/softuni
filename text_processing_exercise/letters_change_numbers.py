text = input().split()
final_sum = 0

for word in text:
    word = word.strip()
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:len(word)-1])

    if first_letter.isupper():
        final_sum += number / (ord(first_letter)-64)
    elif first_letter.islower():
        final_sum += number * (ord(first_letter)-96)

    if last_letter.isupper():
        final_sum -= (ord(last_letter)-64)
    elif last_letter.islower():
        final_sum += (ord(last_letter)-96)

print(f'{final_sum:.2f}')