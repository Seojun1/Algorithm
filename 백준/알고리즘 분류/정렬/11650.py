import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    arr.append([a, b])
arr = sorted(arr)

for j in arr:
    print(j[0], j[1])