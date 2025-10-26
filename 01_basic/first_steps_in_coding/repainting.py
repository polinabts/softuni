nylon = 1.50
paint = 14.50
tiner = 5.00

nylon_needed = int (input())
paint_needed = int (input())
tiner_needed = int (input())
constructor_hour = int (input())

nylon_total = nylon_needed + 2
paint_total = paint_needed * 1.1

material_price = (nylon * nylon_total) + 0.4 + (paint_total * paint) + (tiner * tiner_needed)
constructor_price_per_hour = material_price * 0.30
constructor_price = constructor_price_per_hour * constructor_hour
repainting_price = material_price + constructor_price

print (repainting_price)