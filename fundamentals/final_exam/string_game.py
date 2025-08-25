string_to_change = input()
new_string = string_to_change

while True:

    if string_to_change == "Done":
        break

# On the following lines, you will be receiving commands until the "Done" command.
# There are six possible commands:
    data = string_to_change.split()
    current_command = data[0]
# •	"Change {char} {replacement}"
# o	Replace all occurrences of the char with the given replacement, then print the string.
    if current_command == "Change":
        new_string = new_string.replace(data[1], data[2])
        print(new_string)
# •	"Includes {substring}"
# o	Check if the string includes the given substring with and print "True" or "False".
    elif current_command == "Includes":
        if data[1] in new_string:
            print("True")
        else:
            print("False")
# •	"End {substring}"
# o	Check if the string ends with the given substring and print "True" or "False".
    elif current_command == "End":
        if new_string.endswith(data[1]):
            print("True")
        else:
            print("False")
# •	"Uppercase"
# o	Make the whole string uppercased, then print it.
    elif current_command == "Uppercase":
        new_string = new_string.upper()
        print(new_string)
# •	"FindIndex {char}"
# o	Find the index of the first occurrence of the given char, then print it.
    elif current_command == "FindIndex":
        index = new_string.find(data[1])
        print(index)
# •	"Cut {startIndex} {count}"
# o	Remove all characters from the string, except those starting from the given start index and the next count of characters.
# Print only the cut chars.
    elif current_command == "Cut":
        new_word = new_string[int(data[1]) : int(data[1]) + int(data[2])]
        print(new_word)

    string_to_change = input()
