budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
bread_price = eggs_price + flour_price + (milk_price * 0.25)

colored_eggs = 0
number_of_loaves = 0

while bread_price < budget:

    colored_eggs += 3
    number_of_loaves += 1

    if number_of_loaves % 3 == 0:
        if colored_eggs - (number_of_loaves - 2) < 0:
            break
        else:
            colored_eggs = colored_eggs - (number_of_loaves - 2)

budget -= bread_price

print (f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
