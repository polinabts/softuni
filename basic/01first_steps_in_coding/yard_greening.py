sq_meters = float (input())

price = sq_meters * 7.61
discount = price * 0.18

total_price = price - discount


print (f"The final price is: {total_price} lv.")
print (f"The discount is: {discount} lv.")