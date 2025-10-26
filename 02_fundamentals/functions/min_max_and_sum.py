sequence_of_numbers = input().split()
numbers_list = list(map(int, sequence_of_numbers))

minimum_number = min(numbers_list)
maximum_number = max(numbers_list)
sum_of_all_numbers = sum(numbers_list)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
