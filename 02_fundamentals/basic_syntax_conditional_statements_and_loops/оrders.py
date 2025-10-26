order_num = int (input())
total_price = 0

for _ in range (order_num):

    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if capsule_price <0.01 or capsule_price > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if capsule_per_day < 1 or capsule_per_day > 2000:
        continue

    order_price = capsule_price * days * capsule_per_day
    print (f"The price for the coffee is: ${order_price:.2f}")

    total_price += order_price

print (f"Total: ${total_price:.2f}")