string_number = int(input())

for current_strings in range (string_number):
    current_string = input()
    if "," in current_string \
            or "." in current_string \
            or "_" in current_string:
        print (f"{current_string} is not pure!")
    else:
        print (f"{current_string} is pure.")
