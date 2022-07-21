import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    a, b = list(map(str, sys.stdin.readline().split()))
    arr.append([a, i, b])

for j in range(N):
    arr[j][0] = int(arr[j][0])
arr.sort()
for j in range(N):
    del arr[j][1]

for i in range(N):
    print(arr[i][0], arr[i][1])