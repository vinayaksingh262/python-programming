# f = open("C:\\Users\\DELL\\Documents\\python programming\\codeanddebug\\hello.txt")

# x = f.read()
# print(x)
# f.close()

with open(
    "C:\\Users\\DELL\\Documents\\python programming\\codeanddebug\\hello.txt"
) as f:
    x = f.read()
    for ch in x:
        print(ch)
