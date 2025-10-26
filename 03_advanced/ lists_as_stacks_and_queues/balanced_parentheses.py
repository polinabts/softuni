data = input()
par_stack = []

parenthesis = {"(" : ")", "[" : "]", "{" : "}"}

balanced = True

for letter in data:
    if letter in parenthesis:
        par_stack.append(letter)
    elif letter in parenthesis.values():
        if not par_stack:
            balanced = False
            break
        last = par_stack.pop()
        if parenthesis[last] != letter:
            balanced = False
            break


if par_stack:
    balanced = False

print("YES" if balanced else "NO")