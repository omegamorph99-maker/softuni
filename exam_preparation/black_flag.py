days_of_raids = int(input())
plunder_per_day = int(input())
expected_number = int(input())

final_plunder = 0
days = 0

while days < days_of_raids:
    days += 1
    final_plunder += plunder_per_day

    if days % 3 == 0:
        final_plunder += plunder_per_day * 0.5

    if days % 5 == 0:
        final_plunder *= 0.7


if final_plunder >= expected_number:
    print(f'Ahoy! {final_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {(final_plunder / expected_number * 100):.2f}% of the plunder.')