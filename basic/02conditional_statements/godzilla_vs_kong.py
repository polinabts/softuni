#Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
budget = float (input())
mute_number = int (input())
mute_dressing = float (input())

mute_dressing_price = mute_dressing * mute_number
decore_price = budget * 0.10

 # •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
if mute_number >= 150:
    mute_dressing_price = mute_dressing_price * 0.90

movie_money = mute_dressing_price + decore_price

# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
if movie_money > budget:
    money_needed = movie_money - budget
    print ("Not enough money!")
    print (f"Wingard needs {money_needed:.2f} leva more.")

# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.
else:
    money_left = budget - movie_money
    print ("Action!")
    print (f"Wingard starts filming with {money_left:.2f} leva left.")