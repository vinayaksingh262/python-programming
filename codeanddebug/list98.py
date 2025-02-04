# sum of  the even numbers present in list
x = [1, 2, 3, 4, 5, 6, 7, 8]
total = 0
for i in range(0, len(x)):
    if x[i] % 2 == 0:
        total = total + x[i]
print(total)
