capacity = int(input())

def add(users_dict, data_entry):
    username = data_entry[1]
    sent = data_entry[2]
    received = data_entry[3]
    if username not in users_dict:
        users_dict[username] = {"sent": int(sent), "received": int(received)}
    return users_dict

def message(users_dict, data_entry):
    sender = data_entry[1]
    receiver = data_entry[2]
    if sender in users_dict and receiver in users_dict:
        users_dict[sender]["sent"] += 1
        if (users_dict[sender]["sent"] + users_dict[sender]["received"]) >= capacity:
            del users_dict[sender]
            print(f"{sender} reached the capacity!")

        users_dict[receiver]["received"] += 1
        if (users_dict[receiver]["sent"] + users_dict[receiver]["received"]) >= capacity:
            del users_dict[receiver]
            print(f"{receiver} reached the capacity!")

    return users_dict

def empty(users_dict, data_entry):
    username = data_entry[1]
    if username in users_dict:
        del users_dict[username]
    if username == "All":
        users_dict = {}

    return users_dict

users = {}
command = input()

while command != "Statistics":
    data = command.split("=")
    mapping = {
        "Add": add,
        "Message": message,
        "Empty": empty
    }
    current_command = data[0]

    users = mapping[current_command](users, data)
    command = input()

users_count = len(users)
print(f"Users count: {users_count}")
for k, v in users.items():
    print(f"{k} - {v['sent'] + v['received']}")
