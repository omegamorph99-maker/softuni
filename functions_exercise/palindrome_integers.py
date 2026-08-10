def is_palindrome(number: str) -> bool:
    return number == number[::-1]

list_of_positive_integers = input().split(', ')
for character in list_of_positive_integers:
    print(is_palindrome(character))
