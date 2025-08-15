# Q. print the sum of 1 to N numbers


# 1 using parameter recursion


def fun(sum, i, N):
    if i > N:
        print(sum)
        return
    fun(sum + i, i + 1, N)


fun(0, 1, 4)

# 2 using functional recursion


def fun(N):
    if N == 1:
        return 1
    return N + fun(N - 1)


x = fun(4)
print(x)
