"""
Write a function that takes a three numbers as perameters  and print largest amongs them

"""


def largest(n1, n2, n3):
    if n1 > n2 and n1 > n3:

        print(f"{n1} is largest...")
    elif n2 > n1 and n2 > n3:

        print(f"{n2} is largest...")
    else:

        print(f"{n3} is largest...")


largest(10, 10, 10)
