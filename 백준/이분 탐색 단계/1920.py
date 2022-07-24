def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left+right) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

N = int(input())
M = sorted(list(map(int, input().split())))
N2 = int(input())
M2 = list(map(int, input().split()))

for i in M2:
    idx = binary_search(M, i)
    if idx == 1:
        print(1)
    else:
        print(0)