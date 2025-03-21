num = [1, 2, 1, 2, 4, 5, 7, 8, 7, 8, 9, 9]
freq_map = {}
for i in range(0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1
print(freq_map)
