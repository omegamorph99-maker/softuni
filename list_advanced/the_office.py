employ_happiness = list(map(int, input().split()))
factor = int(input())

multiplied_happiness = list(employ * factor for employ in employ_happiness)
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_employs = sum(happiness >= average_happiness for happiness in multiplied_happiness)

if happy_employs >= (len(multiplied_happiness) / 2):
    print(f'Score: {happy_employs}/{len(multiplied_happiness)}. Employees are happy!')
else:
    print(f'Score: {happy_employs}/{len(multiplied_happiness)}. Employees are not happy!')
