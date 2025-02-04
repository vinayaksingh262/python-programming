"""WAP that has two list and make a new list that contains only the common elements between them"""

lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = [5, 6, 7, 8, 9]
result = []
for num in lst1:
    if num in lst2:
        if num not in result:
            result.append(num)
print(result)
