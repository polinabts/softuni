number_letters = int(input())

for first_letter in range (97, 97 + number_letters):
    for second_letter in range(97, 97 + number_letters):
        for third_letter in range(97, 97 + number_letters):

            print (f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}")
