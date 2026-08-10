budget = float(input())
kg_flour = float(input())
pack_of_eggs = kg_flour * 0.75
milk = (kg_flour * 1.25) / 4
bread_price = kg_flour + pack_of_eggs + milk
loaf_count = 0
total_cost = 0
coloured_eggs = 0

while total_cost < ( budget - bread_price ) :
    total_cost += bread_price
    loaf_count += 1
    coloured_eggs +=3
    if loaf_count % 3 == 0:
        coloured_eggs = coloured_eggs - (loaf_count - 2)

print(f'You made {loaf_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and {(budget - total_cost):.2f}BGN left.')