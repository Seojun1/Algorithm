# 소트인사이드
N = list(map(int, input()))
N.sort()
N.reverse()
for i in N:
    print(i, end='')