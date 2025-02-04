"""
WAP to remove even no i list
"""

# method 1
x = [5, 10, 15, 20, 15]
y = []
for i in x:
    if i % 2 != 0:
        y.append(i)
print(y)

# method 2

for i in range(len(x) - 1, -1, -1):
    if x[i] % 2 == 0:
        x.pop(i)
print(x)
