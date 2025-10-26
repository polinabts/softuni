command = input()
chat_msg = list()

while command != "end":
    messages = command.split()
    command = messages[0]
    message = messages[1]

    if command == "Chat":
        chat_msg.append(message)

    elif command == "Delete":
        if message in chat_msg:
            chat_msg.remove(message)

    elif command == "Edit":
        new_msg = messages[2]
        if message in chat_msg:
            index = chat_msg.index(message)
            chat_msg[index] = new_msg

    elif command == "Pin":
        if message in chat_msg:
            index = chat_msg.index(message)
            message = chat_msg.pop(index)
            chat_msg.append(message)

    elif command == "Spam":
        for i in range(1, len(messages)):
            chat_msg.append(messages[i])

    command = input()

print("\n".join(chat_msg))
