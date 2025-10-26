from collections import deque
from datetime import datetime, timedelta


robots_data = input().split(";")
start_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()
while True:
    line = input()
    if line == "End":
        break
    products.append(line)

robots = []
for data in robots_data:
    name, time = data.split("-")
    robots.append([name, int(time), 0])

current_time = start_time
while products:
    current_time += timedelta(seconds=1)
    product = products.popleft()

    for robot in robots:
        if robot[2] > 0:
            robot[2] -= 1

    for robot in robots:
        if robot[2] == 0:
            robot[2] = robot[1]
            print(f"{robot[0]} - {product} [{current_time.strftime('%H:%M:%S')}]")
            break
    else:
        products.append(product)