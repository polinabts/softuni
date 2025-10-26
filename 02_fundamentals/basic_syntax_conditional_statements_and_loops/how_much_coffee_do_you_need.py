command = input()
coffe_needed = 0

while command != "END":

    if (command == "coding"
            or command == "dog"
            or command == "cat"
            or command == "movie"):
        coffe_needed += 1
    elif (command == "coding".upper()
        or command == "dog".upper()
        or command == "cat".upper()
        or command == "movie".upper()):
        coffe_needed += 2

    command = input()

if coffe_needed > 5:
    print ("You need extra sleep")
else:
    print (coffe_needed)