import sys
N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
N2 = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left+right) // 2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

for i in arr2:
    idx = binary_search(arr, i)
    if idx == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')