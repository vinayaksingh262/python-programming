"""
Make a list and remove duplicate elements from list

"""

x = [5, "Anu", 5, 4, 3, 2, 1, 1, "Anu"]
result = []
for i in x:
    if i not in result:
        result.append(i)

print(result)
