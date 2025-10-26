from collections import deque

queue = deque()
green_light_duration = int(input())
free_window = int(input())
total_cars_passed = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    if command != "green":
        queue.append(command)
    else:
        current_green = green_light_duration

        while queue and current_green > 0:
            car = queue.popleft()
            car_length = len(car)

            if car_length <= current_green:
                total_cars_passed += 1
                current_green -= car_length
            else:
                time_left = current_green + free_window
                if car_length <= time_left:
                    total_cars_passed += 1
                else:
                    hit_index = time_left
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()
                break