def bubble_search(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

nums = [2, 3, 1, 7, 5, 4, 9, 8]
print(f'[original list] = {nums}')
bubble_search(nums)
print(f'[after Bubble] = {nums}')