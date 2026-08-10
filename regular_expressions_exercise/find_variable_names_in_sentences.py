import re

text = input()

rule = r'\b_([a-zA-Z0-9]+)\b'

match = re.findall(rule, text)

print(','.join(match))