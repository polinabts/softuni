list_num_as_string = input().split(" ")
number = int(input())

new_list = list(map(int, list_num_as_string))

for _ in range (number):
    new_list.remove(min(new_list))

new_list = list(map(str, new_list))
print(", ".join(new_list))






