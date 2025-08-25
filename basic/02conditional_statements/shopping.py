# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
# vhod
# 1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [1…100]
# 3.	Броят процесори - цяло число в интервала [1…100]
# 4.	Броят рам памет - цяло число в интервала [1…100]
budget = float (input())
videocard_num = int (input())
proscessor_num = int (input())
ram_num = int (input())

videocard_price = 250.00
videocard_cost = videocard_price * videocard_num
proscessor_price = 0.35 * videocard_cost
ram_price = 0.10 * videocard_cost

cost = videocard_cost + (proscessor_price * proscessor_num) + (ram_price * ram_num)
# . Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
if videocard_num > proscessor_num:
    cost *= 0.85

if cost <= budget:
    print (f"You have {(budget - cost):.2f} leva left!")
elif cost > budget:
    print (f"Not enough money! You need {(cost - budget):.2f} leva more!")
# izhod
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# •	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# •	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичнат