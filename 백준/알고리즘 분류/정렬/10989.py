# 메모리 초과 코드

import sys
N = int(sys.stdin.readline())
a = []
for i in range(N):
    a.append(int(sys.stdin.readline()))

for j in sorted(a):
    print(j)