from math import sqrt


def is_prime(n) -> bool:
    if n < 2:
        return False
    for i in (2, sqrt(n) + 1):
        if n % i == 0:
            return False

    return True


print(is_prime(29))
