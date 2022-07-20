N = int(input())
m = list(map(int, input().split()))
m.sort()

# int형 숫자 뒤집기
m = m[::-1]

for i in m:
    print(i, end=' ')