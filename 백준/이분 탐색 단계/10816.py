from sys import stdin
N = int(stdin.readline())
M = sorted(map(int, stdin.readline().split()))
N2 = int(stdin.readline())
M2 = list(map(int, stdin.readline().split()))

def binary_serach(arr, target):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return arr.count(target)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0
for i in range(len(M2)):
    idx = binary_serach(M, M2[i])
print(idx)