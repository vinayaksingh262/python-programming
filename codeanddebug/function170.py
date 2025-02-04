"""
Write a function that takes a list and print the sum of all elements of list and also find the average of elements

"""


def sum_lst(lst):
    total = 0
    for i in lst:
        total += i
    print(f"total of all numbers {total}")
    avg = total / len(lst)
    print(f"average of all numbers {avg}")


sum_lst([10, 20, 30, 40, 50])
