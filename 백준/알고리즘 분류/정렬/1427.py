# 소트인사이드
import sys
N = sys.stdin.readline()
N = sorted(N)
for i in range(len(N) -1 , 0-1, -1):
    print(N[i], end='')