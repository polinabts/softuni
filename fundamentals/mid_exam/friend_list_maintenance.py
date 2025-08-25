name_lst = input().split(", ")
command = input().split()
blacklisted_names = 0
lost_names = 0

while command[0] != "Report":

    if command[0] == "Blacklist":
        name = command[1]
        if name not in name_lst:
            print(f"{name} was not found.")
        else:
            name_inx = name_lst.index(name)
            name_lst[name_inx] = "Blacklisted"
            print(f"{name} was blacklisted.")
            blacklisted_names += 1

    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(name_lst):
            if name_lst[index] not in ("Blacklisted", "Lost"):
                name = name_lst[index]
                name_lst[index] = "Lost"
                print (f"{name} was lost due to an error.")
                lost_names += 1

    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(name_lst):
            current_name = name_lst[index]
            name_lst[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

    command = input().split()

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(name_lst))
