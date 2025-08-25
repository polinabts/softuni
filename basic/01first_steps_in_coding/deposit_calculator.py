# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]

deposit_sum = float(input())
deposit_time = int (input())
interest = float (input())

# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
# sum_all_time = deposit_sum + deposit_time * ((deposit_sum * interest) / 12)
interest_per_month = ((deposit_sum * interest) / 12) / 100
sum_all_time = deposit_sum + (deposit_time * interest_per_month)

print (sum_all_time)
