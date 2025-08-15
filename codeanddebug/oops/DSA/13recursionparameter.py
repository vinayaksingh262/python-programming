def fun(x, N):
    if N == 0:
        return
    print(x)
    fun(x, N - 1)


fun(15, 4)

"""problem---
print 1 to N using recursion"""


def fun(x, N):
    if x == N + 1:
        return
    print(x)
    fun(x + 1, N)


fun(1, 10)
