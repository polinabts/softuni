year_tax = int (input())

snickers_price = year_tax * 0.60
sportswear = snickers_price * 0.80
ball = sportswear * 0.25
accessories = ball * 0.20

price = year_tax + snickers_price + sportswear + ball + accessories

print (float (price))