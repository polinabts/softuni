initial_energy = int(input())
battle_count = 0
# battle_won = 0
#
# if initial_energy > 10000:
#     initial_energy = 10000
# elif initial_energy < 1:
#     initial_energy = 1

while True:
    distance = input()

    if distance == "End of battle":
        print(f"Won battles: {battle_count}. Energy left: {initial_energy}")
        break

    # if int(distance) > 10000:
    #     distance = 10000
    # elif int(distance) < 1:
    #     distance = 1

    if initial_energy - int(distance) < 0:
        print(f"Not enough energy! Game ends with {battle_count} won battles and {initial_energy} energy")
        break

    initial_energy -= int(distance)

    if initial_energy >= 0:
        battle_count += 1
        # battle_won += 1

    if battle_count % 3 == 0:
        initial_energy += battle_count
        # battle_won = 0

