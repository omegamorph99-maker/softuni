import re

text = input()

patter = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

result = re.findall(patter, text)

print(' '.join(result))