from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

free_flour = students // 5
flour_cost = (students * price_flour) - (free_flour * price_flour)
egg_cost = students * price_egg * 10
apron_cost = price_apron * ceil(students * 1.2)
item_cost = flour_cost + egg_cost + apron_cost

if item_cost <= budget:
    print(f"Items purchased for {item_cost:.2f}$.")
else:
    needed_money = item_cost - budget
    print(f"{needed_money:.2f}$ more needed.")