divisor = int (input())
boundary = int (input())

number = 0
for i in range (0, boundary + 1):

    if i % divisor == 0:
        if i > number:
            number = i

print (number)
