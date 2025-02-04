"""
Write a function that accepts an integer and prints whether it is odd or even
"""


def evenOdd():
    n = int(input("Enter number to check even or odd ="))
    if n % 2 == 0:
        print(f"{n} is even...")
    else:
        print(f"{n} is odd...")


evenOdd()
