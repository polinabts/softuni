ingredients = input().split(" ")
bakery = {}
# bread 10 butter 4 sugar 9 jam 12
for i in range (0, len(ingredients), 2):
    key = ingredients[i]
    value = ingredients[i + 1]
    bakery[key] = int(value)

print(bakery)