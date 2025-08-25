budget = int (input())
command = input()

while command != "End":
    price = int (command)
    if budget - price < 0:
        print ("You went in overdraft!")
        break
    budget -= price
    command = input()

if command == "End":
    print ("You bought everything needed.")


