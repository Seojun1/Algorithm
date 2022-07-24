def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

N = int(input())
M = sorted(list(map(int, input().split())))
N2 = int(input())
M2 = list(map(int, input().split()))

for i in M2:
    idx = binary_search(M, i)
    if idx == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')