def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)
