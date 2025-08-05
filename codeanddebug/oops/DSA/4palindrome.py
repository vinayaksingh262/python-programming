# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
# Therefore it is not a palindrome.


# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    num = x
    palindrome_no = 0
    while num > 0:
        last_digit = num % 10
        palindrome_no = (palindrome_no * 10) + last_digit
        num = num // 10
    return palindrome_no == x


print(is_palindrome(520))
