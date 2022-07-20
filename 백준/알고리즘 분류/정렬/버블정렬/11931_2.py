# 내림차순

import sys
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    a = int(sys.stdin.readline())
    arr.append(a)

def bubble(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    for e in range(n):
        print(array[e])

bubble(arr)