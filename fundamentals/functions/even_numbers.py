numbers_as_string = input().split()
numbers_as_digits = list(map(int, numbers_as_string))
print (list(filter(lambda x: x % 2 == 0, numbers_as_digits)))
