first_char_index = int(input())
last_char_index = int(input())

for character in range (first_char_index, last_char_index +1):
    if character == last_char_index:
        print (chr(last_char_index))
    else:
        print (chr(character), end =" ")