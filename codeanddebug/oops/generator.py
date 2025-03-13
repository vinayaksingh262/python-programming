def my_gen():
    for i in range(10):
        yield i


obj = my_gen()
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
for j in obj:
    print(j)
