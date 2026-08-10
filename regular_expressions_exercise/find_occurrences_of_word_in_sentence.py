import re

text = input()
searching_for = input()

rule = fr'\b{searching_for}\b'

match = re.findall(rule, text, re.IGNORECASE)

print(len(match))