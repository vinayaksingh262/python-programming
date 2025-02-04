"""
Write a function that accepts an integer and prints the multiplication 
table for that number upto 10
"""

# method 1


def multiplicationTsble():
    n = int(input("Enter a number you want to print multiplication table ="))
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")


multiplicationTsble()


# method 2
# def multiplicatioTable(num):
#     for i in range(1, 11):
#         print(f"{num} * {i} = {num*i}")


# multiplicatioTable(10)
