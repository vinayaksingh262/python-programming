def third_largest(arr):
    if len(arr) < 3:
        return "array must have atleast three element."
    arr = list(set(arr))
    arr.sort(reverse=True)
    return arr[2]


array = list(map(int, input("Enter numbers").split()))
print("third largest number:", third_largest(array))
