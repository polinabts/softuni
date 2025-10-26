from collections import deque


food_quantity = int(input())

food_per_order = input().split()
food_int = deque(map(int, food_per_order))
print(max(food_int))

while food_quantity > 0 and food_int:
    if food_int and food_quantity - food_int[0] >= 0:
        order = food_int.popleft()
        food_quantity -= order
    else:
        print(f"Orders left: {' '.join(deque(map(str, food_int)))}")
        exit()

print("Orders complete")
