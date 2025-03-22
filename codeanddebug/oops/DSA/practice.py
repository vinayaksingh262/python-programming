# frequency map
# method 1

num = [1, 2, 1, 2, 4, 5, 7, 8, 7, 8, 9, 9]
freq_map = {}
for i in range(0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1
print(freq_map)


# method 2

hash_map = {}
n = len(num)
for i in range(0, n):
    hash_map[num[i]] = hash_map.get(num[i], 0) + 1
print(hash_map)

# method3

from collections import Counter

print(dict(Counter(num)))
