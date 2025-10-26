def sum_of_numbers(number: str) -> tuple:
    odd_digits = 0
    even_digits = 0

    for index in range(len(number)):
        current_number = int(number[index])
        if current_number %2 == 0:
            even_digits += current_number
        else:
            odd_digits += current_number

    return odd_digits, even_digits

single_number = input()
sum_of_odd_digits, sum_of_even_digits = sum_of_numbers(single_number)
print (f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")