number_of_lines = int(input())
synonyms = {}

for i in range(number_of_lines):
    word = input()
    synonym = input()

    if word not in synonyms.keys():
        synonyms[word] = [synonym]
    else:
        synonyms[word].append(synonym)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")