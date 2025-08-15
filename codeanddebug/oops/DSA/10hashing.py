# method 1
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
hash_lst = [0] * 11
for i in n:
    hash_lst[i] += 1
for i in m:
    if i < 0 or i > 10:  # time complexity - O(m+n)
        print(0)
    else:
        print(hash_lst[i], end=" ")

# method 2
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
hash_map = dict()
for i in range(0, len(n)):
    hash_map[n[i]] = hash_map.get(n[i], 0) + 1
for x in m:
    print("the no.", x, "appears", hash_map.get(x, 0), "times.")
