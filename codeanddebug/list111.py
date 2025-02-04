"""
Make a list then ask a number of a user if umber exist in that list 
then print the position of the element else -1"""

x = [50, 55, 56, 57, 58, 59, 60]
value = int(input("Enter the value to print its position:"))

if value in x:
    index = x.index(value)
    print(index)
else:
    print(-1)
