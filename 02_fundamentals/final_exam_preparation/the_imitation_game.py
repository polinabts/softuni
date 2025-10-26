message = input()

new_message = message

while True:

    if message == "Decode":
        break

    entry = message.split("|")
    current_command = entry[0]

    if current_command == "Move":
        index = int(entry[1])
        new_message = new_message[index:] + new_message[:index]

    elif current_command == "Insert":
        index = int(entry[1])
        new_message = new_message[:index] + entry[2] + new_message[index:]

    elif current_command == "ChangeAll":
        substring = entry[1]
        replacement = entry[2]
        new_message = new_message.replace(substring, replacement)

    message = input()

print(f"The decrypted message is: {new_message}")




# def move(text, number_of_letters):
#     number_of_letters = int(number_of_letters)
#     return text[number_of_letters:] + text[:number_of_letters]
#
#
# def insert(text, index, value):
#     index = int(index)
#     return text[:index] + value + text[index:]
#
#
# def change_all(text, substring, replacement):
#     return text.replace(substring, replacement)
#
#
# def decode_message(encrypted_message):
#     while True:
#         command = input()
#         if command == "Decode":
#             break
#
#         parts = command.split("|")
#         action = parts[0]
#
#         if action == "Move":
#             encrypted_message = move(encrypted_message, parts[1])
#         elif action == "Insert":
#             encrypted_message = insert(encrypted_message, parts[1], parts[2])
#         elif action == "ChangeAll":
#             encrypted_message = change_all(encrypted_message, parts[1], parts[2])
#
#     return encrypted_message
#
#
# # --- MAIN PROGRAM ---
# initial_message = input()
# final_message = decode_message(initial_message)
# print(f"The decrypted message is: {final_message}")