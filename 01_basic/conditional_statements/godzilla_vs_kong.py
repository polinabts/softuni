budget = float (input())
mute_number = int (input())
mute_dressing = float (input())

mute_dressing_price = mute_dressing * mute_number
decore_price = budget * 0.10

if mute_number >= 150:
    mute_dressing_price = mute_dressing_price * 0.90

movie_money = mute_dressing_price + decore_price

if movie_money > budget:
    money_needed = movie_money - budget
    print ("Not enough money!")
    print (f"Wingard needs {money_needed:.2f} leva more.")

else:
    money_left = budget - movie_money
    print ("Action!")
    print (f"Wingard starts filming with {money_left:.2f} leva left.")