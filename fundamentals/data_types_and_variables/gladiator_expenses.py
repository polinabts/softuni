lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = lost_fights_count // 2
sword_broken = lost_fights_count // 3
shield_broken = lost_fights_count // (2 * 3)
armor_broken = shield_broken // 2

total_expenses = (helmet_price * helmet_broken +
                  sword_broken * sword_price +
                  shield_price * shield_broken +
                  armor_price * armor_broken)

print (f"Gladiator expenses: {total_expenses:.2f} aureus")