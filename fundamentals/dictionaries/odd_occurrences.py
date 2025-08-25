# words = input().split()
# elements = {}
# result  = []
#
# for word in words:
#     word = word.lower()
#     # if word not in elements:
#     #     elements[word] = 1
#     # else:
#     #     elements[word] += 1
#     elements[word] = elements.get(word, 0) + 1
#
# for key, value in elements.items():
#     if value % 2 == 1:
#         result.append(key)
#
# print(" ".join(result))

from collections import Counter

words = input().lower().split()
counts = Counter(words)

result = [word for word, count in counts.items() if count % 2 == 1]
print(" ".join(result))
