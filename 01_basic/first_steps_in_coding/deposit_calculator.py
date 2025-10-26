deposit_sum = float(input())
deposit_time = int (input())
interest = float (input())

interest_per_month = ((deposit_sum * interest) / 12) / 100
sum_all_time = deposit_sum + (deposit_time * interest_per_month)

print (sum_all_time)
