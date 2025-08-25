from math import ceil

people_number = int(input())
elevator_capacity = int(input())
courses = ceil(people_number / elevator_capacity)

print (courses)

