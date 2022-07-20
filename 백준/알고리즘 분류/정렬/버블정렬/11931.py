import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
for i in reversed(sorted(arr)):
    print(i)