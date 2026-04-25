from collections import OrderedDict

words = OrderedDict()
for _ in range(int(input())):
    w = input().strip()
    words[w] = words.get(w, 0) + 1

print(len(words))
print(*(words.values()))
