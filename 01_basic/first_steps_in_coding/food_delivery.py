chicken_price = 10.35
fish_price = 12.40
vegeterian_price = 8.15

chicken_number = int (input())
fish_number = int (input())
vegeterian_number = int (input())

food_price = (chicken_price * chicken_number) + (fish_price * fish_number) + (vegeterian_number * vegeterian_price)
dessert_price = food_price * 0.20
food_total = food_price + dessert_price + 2.50

print (float (food_total))
