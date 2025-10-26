from collections import deque

queue = deque(input().split())
toss_number = int(input()) - 1


while len(queue) > 1:
    queue.rotate(-toss_number)
    name = queue.popleft()
    print(f"Removed {name}")

print(f"Last is {queue[0]}")
