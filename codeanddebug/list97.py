# Count the even numbers present in list
x = [45, 96, 44, 56, 48, 53]
count = 0
for i in x:
    if i % 2 == 0:
        count = count + 1
print(count)
