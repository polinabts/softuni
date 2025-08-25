data = input()
data_list = []

for i, current_char in enumerate(data):

    if current_char.isupper():
        data_list.append(i)
print(data_list)
