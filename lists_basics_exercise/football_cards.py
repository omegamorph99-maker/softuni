team_a = [f'A-{number}' for number in range(1,12)]
team_b = [f'B-{number}' for number in range(1,12)]
terminated = False
cards = input().split()

for card in cards:
    if card in team_a:
        team_a.remove(card)
    if card in team_b:
        team_b.remove(card)

    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if terminated:
    print(f'Game was terminated')