def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fib(5):
    print(num, end=" ")
# time complexity - O(n)
# space complexity - O(1)
