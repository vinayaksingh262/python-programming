# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
#  then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:             # Example 2:           # Example 3:
# Input: x = 123         # Input: x = -123      # Input: x = 120
# Output: 321            # Output: -321         # Output: 21

# Constraints:

# -231 <= x <= 231 - 1


def reverse(x: int) -> int:
    is_negative = False
    if x < 0:
        is_negative = True
    num = abs(x)
    answer = 0
    while num > 0:
        last_digit = num % 10
        answer = (answer * 10) + last_digit
        num //= 10
    if answer < ((-(21**31))) or answer > (2**31 - 1):
        return 0
    return -answer if is_negative else answer


print(reverse(123))
print(reverse(-123))
print(reverse(120))
