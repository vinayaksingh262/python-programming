import math


def lcmandgcd(a: int, b: int) -> list[int]:
    gcd_value = math.gcd(a, b)
    lcm_value = (a * b) // gcd_value
    return [lcm_value, gcd_value]


print(lcmandgcd(14, 8))
