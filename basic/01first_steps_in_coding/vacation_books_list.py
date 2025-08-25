pages_number = int (input())
pages_per_hour = int (input())
days_to_read = int (input())

hours_to_read = int (pages_number / pages_per_hour)
hours_per_day = int (hours_to_read / days_to_read)

print (hours_per_day)
