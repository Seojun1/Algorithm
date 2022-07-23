from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
N2 = int(stdin.readline())
arr2 = list(map(int, stdin.readline().split()))

def binary_search(data, target):
    data.sort()
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left+right) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            left = data[mid] + 1
        else:
            right = data[mid] - 1
    return 0

for i in arr2:
     idx = binary_search(arr, i)
     if idx == 1:
         print(1)
     else:
         print(0)