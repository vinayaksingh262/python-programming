# find largest number in list
x = [10, 500, 7788, 5, 6, -3]
largest = x[0]
for i in range(0, len(x)):
    if x[i] > largest:
        largest = x[i]
print(largest)
