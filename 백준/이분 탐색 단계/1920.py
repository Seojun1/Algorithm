import sys
N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
N2 = int(sys.stdin.readline())
M2 = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for i in M2:
    idx = binary_search(M, i)
    if idx == 1:
        print(1)
    else:
        print(0)