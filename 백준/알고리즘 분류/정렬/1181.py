# 단어 정렬
import sys
N = int(sys.stdin.readline())
a = []
for i in range(N):
    a.append(input())
arr = list(set(a))

sort_arr = []
for i in arr:
    sort_arr.append((len(i), i))
sort_arr = sorted(sort_arr)

for j in sort_arr:
    print(j[1])