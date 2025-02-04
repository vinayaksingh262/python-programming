# print all the values which are present in even positions
x = [15, "VS", 65, 94, 63.333]
for i in range(0, len(x)):
    if i % 2 == 0:
        print(x[i], end=" ")
