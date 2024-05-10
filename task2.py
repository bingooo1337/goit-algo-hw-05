def binary_search(arr, target):
    if len(arr) == 0:
        return 0, None

    low_index = 0
    high_index = len(arr) - 1
    iterations = 0

    while low_index <= high_index:
        iterations += 1

        mid_index = (low_index + high_index) // 2
        mid_value = arr[mid_index]

        if mid_value < target:
            low_index = mid_index + 1
        elif mid_value > target:
            high_index = mid_index - 1
        else:
            return iterations, mid_value

    if high_index < 0:
        return iterations, arr[0]
    else:
        return iterations, arr[low_index] if low_index < len(arr) else None


arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
for target in [1, 3.5, 4.6, 5.9, 10]:
    print(binary_search(arr, target))
