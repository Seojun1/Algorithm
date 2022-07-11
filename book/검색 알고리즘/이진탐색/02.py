def bin_search(arr, key):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid -1
        else:
            left = mid + 1

nums = [1, 2, 3, 4, 5, 6]
print(f'x[{bin_search(nums, 6)}]에 위치해있습니다.')