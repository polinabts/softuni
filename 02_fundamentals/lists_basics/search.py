n = int(input())
word = input()
strings = []

for i in range (n):
    current_string = input()
    strings.append(current_string)
print(strings)

for i in range (len(strings)-1, -1, -1):
    element = strings [i]
    if word not in element:
        strings.remove(element)
print(strings)

# 2nd approach / comprehension
# n = int(input())
# word = input()
#
# string = [input() for _ in range(n)]
# filtered_string = [current_string for current_string in string if word in current_string]
#
# print(string)
# print(filtered_string)

