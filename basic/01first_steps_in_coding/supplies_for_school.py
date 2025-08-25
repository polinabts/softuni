pen = 5.80
marker = 7.20
cleanser = 1.20

pen_number = int (input())
marker_number = int (input())
cleanser_liter = int (input())
discount_percent = float (input())

pen_price = pen_number * pen
marker_price = marker * marker_number
cleanser_price = cleanser * cleanser_liter
price = pen_price + marker_price + cleanser_price
discount = price * (discount_percent / 100)
sum_all = price - discount

print (float (sum_all))
