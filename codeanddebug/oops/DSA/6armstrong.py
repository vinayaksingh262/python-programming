def armstrong(n: int) -> bool:
    num = n
    total = 0
    nod = len(str(n))
    while num > 0:
        last_digit = num % 10
        total = total + (last_digit**nod)
        num = num // 10
    return total == n


print(armstrong(153))
print(armstrong(159))
print(armstrong(1634))
