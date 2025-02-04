# print even no in list
a = map(int, input().split())
b = list(a)
print(b)
x = [45, 96, 44, 56, 48, 53]

# method 1 -

for i in range(0, len(x)):
    if x[i] % 2 == 0:
        print(x[i], end=" ")
print("\n")

# method 2 -
for i in x:
    if i % 2 != 0:
        print(i, end=" ")
