# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

# 1.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.	Брой пъзели - цяло число в интервала [0… 1000]
# 3.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.	Брой миньони - цяло число в интервала [0 … 1000]
# 6.	Брой камиончета - цяло число в интервала [0 … 1000]
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

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
if toys_count >= 50:
    toys_total = toys_total * 0.75

rent = toys_total * 0.10
profit = toys_total - rent

# •	Ако парите са достатъчни се отпечатва:
# o	"Yes! {оставащите пари} lv left."
# •	Ако парите НЕ са достатъчни се отпечатва:
# o	"Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

if profit >= excursion:
    money_left = profit - excursion
    print (f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = excursion - profit
    print (f"Not enough money! {money_needed:.2f} lv needed.")