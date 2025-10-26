current_year = int(input())
current_year += 1
while True:
    current_year_as_string = str(current_year)
    if len(set(current_year_as_string)) == len(current_year_as_string):
        break
    current_year += 1
print (current_year)