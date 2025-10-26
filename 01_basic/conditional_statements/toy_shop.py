puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

excursion = float (input())
puzzle_count = int (input())
doll_count = int (input())
bear_count = int (input())
minion_count = int (input())
truck_count = int (input())
toys_count = puzzle_count + doll_count + bear_count + minion_count + truck_count

puzzle_total = puzzle_price * puzzle_count
doll_total = doll_price * doll_count
bear_total = bear_price * bear_count
minion_total = minion_price * minion_count
truck_total = truck_price * truck_count
toys_total = puzzle_total + doll_total + bear_total + minion_total + truck_total

if toys_count >= 50:
    toys_total = toys_total * 0.75

rent = toys_total * 0.10
profit = toys_total - rent

if profit >= excursion:
    money_left = profit - excursion
    print (f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = excursion - profit
    print (f"Not enough money! {money_needed:.2f} lv needed.")