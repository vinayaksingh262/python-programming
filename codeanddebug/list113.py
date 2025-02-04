lst = []
n = int(input("Enter number of elements:"))
for i in range(n):
    x = int(input(f"Enter the value at {i}:"))
    lst.append(x)


lst1 = sum(lst)
print(lst1 / len(lst))
