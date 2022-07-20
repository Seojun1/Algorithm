def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(arr)

nums = [3, 1, 5, 2, 7]
bubble_sort(nums)
for i in nums:
    print(i)