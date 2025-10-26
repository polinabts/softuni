num_queries = int(input())
stack = []

for _ in range(num_queries):
    data = input().split()
    if data[0] == "1":
        stack.append(int(data[1]))
    elif data[0] == "2":
        if stack:
            stack.pop()
    elif data[0] == "3":
        print(max(stack))
    elif data[0] == "4":
        print(min(stack))

strings = list(map(str, stack))
print(", ".join(reversed(strings)))