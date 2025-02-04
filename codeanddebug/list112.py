"""
Take 10 integers inputs from user and store them in a list .
Now copy all the elements in another list but in reverse order ."""

# method 1


my_list = []

for i in range(0, 10):
    x = int(input(f"Enter the value at {i}:"))

    my_list.append(x)
print(my_list)

y = my_list.copy()
y.reverse()
print(y)


# method 2


my_list = []

for i in range(10):
    x = int(input(f"Enter the value at :"))
    my_list.append(x)

result = []

for i in range(len(my_list) - 1, -1, -1):
    result.append(my_list[i])
print(result)
