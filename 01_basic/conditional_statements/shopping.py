budget = float (input())
videocard_num = int (input())
proscessor_num = int (input())
ram_num = int (input())

videocard_price = 250.00
videocard_cost = videocard_price * videocard_num
proscessor_price = 0.35 * videocard_cost
ram_price = 0.10 * videocard_cost

cost = videocard_cost + (proscessor_price * proscessor_num) + (ram_price * ram_num)

if videocard_num > proscessor_num:
    cost *= 0.85

if cost <= budget:
    print (f"You have {(budget - cost):.2f} leva left!")
elif cost > budget:
    print (f"Not enough money! You need {(cost - budget):.2f} leva more!")
