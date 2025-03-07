# non-tail
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# tail
def tail_factorial(n, result=1):
    if n == 1:
        return result
    else:
        return tail_factorial(n - 1, result * n)


print(tail_factorial(5))
