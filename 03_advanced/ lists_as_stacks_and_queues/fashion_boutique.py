box_of_clothes = input().split()
clothes_stack = list(map(int, box_of_clothes))
rack_capacity = int(input())
working_capacity = rack_capacity
rack_counter = 0

while clothes_stack:
    if rack_capacity == working_capacity:
        rack_counter += 1

    if rack_capacity > clothes_stack[-1]:
        rack_capacity -= clothes_stack[-1]
    elif rack_capacity -  clothes_stack[-1] == 0:
        rack_capacity = working_capacity
    else:
        rack_counter += 1
        rack_capacity = working_capacity
        rack_capacity -= clothes_stack[-1]

    clothes_stack.pop()

print(rack_counter)
