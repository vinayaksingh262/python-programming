def fibo(n):
    if n <= 0:
        return "plz enter positive numbers"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def print_fibo(n):
    for i in range(n + 1):
        print(fibo(i))


n = int(input("enter a number you want to print a fibonnaci series :"))
print_fibo(n)
# this is the recursive method of this code and in this time complexity is O(2^n) so this is not optimized version
