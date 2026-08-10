from math import floor

biscuits_per_day = int(input())
count_of_workers = int(input())
competitor_biscuits = int(input())

total_biscuits = 0
for day in range(1,31):
    if day % 3 == 0:
        total_biscuits += floor(biscuits_per_day * count_of_workers * 0.75)
    else:
        total_biscuits += biscuits_per_day * count_of_workers


percentage = abs(total_biscuits - competitor_biscuits) / competitor_biscuits * 100
print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competitor_biscuits:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")