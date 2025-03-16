# Given a range [m, n] (both inclusive) where 0 ≤ m, n ≤ 10000, find the sum of all integers between m and n.

# Example:

# Input: 0 3

# Output: 6


# Explanation: 0+1+2+3 =6
def sum(m, n):
    return (n * (n + 1) // 2) - (m * (m - 1) // 2)


m, n = map(int, input().split())
print(sum(m, n))
