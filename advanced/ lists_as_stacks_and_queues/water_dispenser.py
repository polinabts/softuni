from collections import deque

liters = int(input())
queue = deque()
person = input()

while person != "Start":
    queue.append(person)
    person = input()

data = input()

while data != "End":
    if data.startswith("refill"):
        liters_to_fill = int(data.split()[-1])
        liters += liters_to_fill
    elif data.isdigit():
        person = queue.popleft()
        liters_wanted = int(data)
        if liters_wanted <= liters:
            liters -= liters_wanted
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    data = input()

print(f"{liters} liters left")