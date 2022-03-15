N = int(input())
all = []
for i in range(N):
    a = list(map(int, input().split()))
    b = a.pop(0)
    print(sum(a) / b)
    # 비율을 구하는 방법?
    