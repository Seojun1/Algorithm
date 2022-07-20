import sys
N = int(input())
array = []
for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    array.append([a, b])
array = sorted(array)

for i in range(N):
    print(array[i][0], array[i][1])