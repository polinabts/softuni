herd = input().split(", ")

if herd[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    new_herd = herd[::-1]
    wolf_index = new_herd.index("wolf")
    print(f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")

# print(herd)