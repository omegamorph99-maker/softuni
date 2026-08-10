import re

text = input()

numbers = []

while text:

    rule = r'\d+'

    match = re.findall(rule, text)
    numbers += match
    text = input()

print(' '.join(numbers))