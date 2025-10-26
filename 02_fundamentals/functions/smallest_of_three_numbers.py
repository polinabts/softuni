def smallest_num(first_num : int, second_num : int, third_num : int):
    list_num = [first_num, second_num, third_num]

    return min(list_num)

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_num(first_num, second_num, third_num))
