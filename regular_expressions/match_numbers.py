import re

text = input()

pattern = r'(?<!\S)-?(?:0|[1-9][0-9]*)(?:\.\d+)?(?!\S)'

result = list(re.findall(pattern, text))

for match in range(len(result)):
    print(''.join(result[match]), end=' ')