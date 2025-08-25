# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър
nylon = 1.50
paint = 14.50
tinner = 5.00

# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон,
# разбира се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30%
# от сбора на всички разходи за материали.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
nylon_needed = int (input())
paint_needed = int (input())
tinner_needed = int (input())
constructor_hour = int (input())

nylon_total = nylon_needed + 2
paint_total = paint_needed * 1.1

material_price = (nylon * nylon_total) + 0.4 + (paint_total * paint) + (tinner * tinner_needed)
constructor_price_per_hour = material_price * 0.30
constructor_price = constructor_price_per_hour * constructor_hour
repainting_price = material_price + constructor_price

# Да се отпечата на конзолата един ред:
# •	"{сумата на всички разходи}"
print (repainting_price)