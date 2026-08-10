lost_fights_count = int(input())
helmet_repair_cost = float(input())
sword_repair_cost = float(input())
shield_repair_cost = float(input())
armor_repair_cost = float(input())

total_helmet_repair = (lost_fights_count // 2) * helmet_repair_cost
total_sword_repair = (lost_fights_count // 3) * sword_repair_cost
total_shield_repair = (lost_fights_count // 3 // 2) * shield_repair_cost
total_armor_repair = (lost_fights_count // 3 // 2 // 2) * armor_repair_cost

total_expense = total_helmet_repair + total_sword_repair + total_shield_repair + total_armor_repair

print(f'Gladiator expenses: {total_expense:.2f} aureus')