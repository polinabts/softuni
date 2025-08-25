water_tank_capacity = 255
number_of_lines = int(input())

for current_line in range (number_of_lines):
    liters_added = int(input())
    if water_tank_capacity < liters_added:
        print("Insufficient capacity!")
        continue
    water_tank_capacity -= liters_added
print(255 - water_tank_capacity)
