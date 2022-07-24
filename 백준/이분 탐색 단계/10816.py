import sys

def binary_search(data, target):
    data.sort()
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

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
N2 = int(sys.stdin.readline())
M2 = list(map(int, sys.stdin.readline().split()))

for i in M2:
    idx = binary_search(M, i)
    if idx == 1:
        print(M.count(i), end=' ')
    else:
        print(0, end=' ')