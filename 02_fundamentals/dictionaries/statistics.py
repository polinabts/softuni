products_dictionary = {}

command = input()
while command != "statistics":
    products = command.split(": ")
    product = products[0]
    quantity = products[1]
    if product in products_dictionary:
        products_dictionary[product] += int(quantity)
    else:
        products_dictionary[product] = int(quantity)
    command = input()

count_all_products = len(products_dictionary.keys())
sum_all_quantities = sum(products_dictionary.values())
# print(products_dictionary)
# print(count_all_products)
# print(sum_all_quantities)

print(f"Products in stock:")
for k, v in products_dictionary.items():
    print(f"- {k}: {v}")
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")

