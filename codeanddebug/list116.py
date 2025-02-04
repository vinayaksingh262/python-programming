"""WAP to print second largest element without using sort fuction"""

# using sort function =
"""
lst = [55, 75, 98, 1, 2, 35, 45, 46, 8, 6, 55, 546, 464, 46]
lst.sort(reverse=True)
print(lst[1])"""

# without using sor function =
lst = [55, 75, 98, 1, 2, 35, 45, 46, 8, 6, 55, 546, 464, 46]
largest = float("-inf")
second_largest = float("-inf")
for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num
print(second_largest)
