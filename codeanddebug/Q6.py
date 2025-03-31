# Xth and Yth Prime Number Calculation Problem Statement: Given two integers X and Y,
# find the Xth and Yth prime numbers in the sequence of prime numbers.
# Then, calculate C using the formula:
# C(AxB)-1
# where A is the Xth prime number and B is the Yth prime number.
# Input: 5 2
# # Output: 32


def nth_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes[-1]


X, Y = map(int, input().split())
A = nth_prime(X)
B = nth_prime(Y)
C = (A * B) - 1
print(C)
