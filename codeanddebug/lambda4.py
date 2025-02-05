lst = [lambda arg=x: arg * 10 for x in range(1, 6)]

for i in lst:
    print(i())
