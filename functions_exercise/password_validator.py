def between_six_and_ten(password: str):
    if 6 <= len(password) <= 10:
        return True
    else:
        return 'Password must be between 6 and 10 characters'

def letters_and_digits(password: str):
    if password.isalnum():
        return True
    else:
        return 'Password must consist only of letters and digits'

def two_digits(password: str):
    number_of_digits = 0
    for digit in password:
        if digit.isdigit():
            number_of_digits += 1

    if number_of_digits >= 2:
        return True
    else:
        return 'Password must have at least 2 digits'


some_password = input()
result = [between_six_and_ten(some_password),letters_and_digits(some_password), two_digits(some_password)]
if all(item is True for item in result):
    print("Password is valid")
else:
    for item in result:
        if item is not True:
            print(item)