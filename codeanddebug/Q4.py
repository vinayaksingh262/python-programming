# Rank Transformation of an Array

# Given an array of integers, replace each element with its rank in the array.
#  The rank of a number is its position in the sorted unique values, with ranks starting from 1.

# Input: 15 8 15 8 25 9
# Output: 3 1  3 1 4 2


def rank_transform(arr):
    unique_sorted = sorted(set(arr))
    rank_dict = {}
    rank = 1
    for num in unique_sorted:
        rank_dict[num] = rank
        rank += 1
    ranked_array = []
    for num in arr:
        ranked_array.append(rank_dict[num])
    return ranked_array


array = list(map(int, input().split()))
print(*rank_transform(array))
