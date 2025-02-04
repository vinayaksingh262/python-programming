# Write a program to split a given list ito two halves.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mid = len(lst) // 2
first_half = lst[:mid]
second_half = lst[mid:]
print(first_half)
print(second_half)
