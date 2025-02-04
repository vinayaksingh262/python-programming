def minimumEffort(arr):
    arr.sort()
    n = len(arr)
    max_effort = 0
    left, right = arr[: n // 2], arr[n // 2 :]
    rearranged = []

    while left or right:
        if right:
            rearranged.append(right.pop())
        if left:
            rearranged.append(left.pop(0))

    for i in range(1, len(rearranged)):
        max_effort = max(max_effort, abs(rearranged))
