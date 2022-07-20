import sys
N = int(input())
array = []
for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    array.append([b, a])
array = sorted(array)

for i in range(N):
    print(array[i][1], array[i][0])