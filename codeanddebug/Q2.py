# Problem Statement:

# You are given an array containing N integers where only one element is unique (appears exactly once), while all other elements appear twice.
#  Find and return the unique element.

# Example:

# Input: arr = [5, 3, 2, 3, 2]


# output:5
def unique_val(arr):
    unique = 0
    for num in arr:
        unique ^= num
    return unique


arr = [5, 3, 2, 3, 2]
print(unique_val(arr))
