N = int(input())
# 오름차순 할 숫자들을 모아놓을 배열 생성
result = []

# 탐색 시작
for _ in range(N):
    a = int(input())
    # result안에 입력받았던 a를 추가
    result.append(a)

# 오름차순
for i in sorted(result):
    print(i)