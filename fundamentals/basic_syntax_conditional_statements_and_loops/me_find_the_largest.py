number = input()
string_list = list(number)
number_list = list(map(int, string_list))

biggest_number = sorted(number_list, reverse=True)
biggest_number_str = map(str, biggest_number)
final_number = "".join(biggest_number_str)
print(final_number)
# pak napishi syshtoto