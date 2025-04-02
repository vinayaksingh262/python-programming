def powerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


print(powerOfTwo(24))
print(powerOfTwo(16))
