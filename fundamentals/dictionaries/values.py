list_characters = input().split(", ")
characters_dictionary = {}

for i in range(len(list_characters)):
    current_char = list_characters[i]
    characters_dictionary[current_char] = ord(current_char)

print(characters_dictionary)