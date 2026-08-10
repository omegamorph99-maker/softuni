secret_message = input().split()
deciphered_message = []

for word in secret_message:
    secret_number = []
    secret_word = []
    for char in word:
        if char.isdigit():
            secret_number.append(char)
        else:
            secret_word.append(char)
    secret_word[0], secret_word[-1] = secret_word[-1], secret_word[0]
    secret_number = int(''.join(secret_number))
    secret_word = ''.join(secret_word)
    deciphered_message.append(chr(secret_number) + secret_word)


print(' '.join(deciphered_message))