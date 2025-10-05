from collections import deque


pump_number = int(input())
pumps = deque()

for _ in range(pump_number):
    current_fuel, distance = map(int, input().split())
    pumps.append((current_fuel, distance))

start = 0
stops = 0

while stops < pump_number:
    fuel = 0
    for current_fuel, distance in pumps:
        fuel += current_fuel
        if fuel < distance:
            pumps.rotate(-1)
            start += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start)