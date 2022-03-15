N = int(input())

# 환경구축
all = []
for i in range(N):
    a = list(map(int, input().split()))
    b = a.pop(0) # 임시의 학생 수는 따로 제외하기
    c = (sum(a) / b) # 평균
    
    # 탐색 시작
    for l in a:
        if (l > c):
            all.append(l)
        else:
            pass
    result = format((len(all) / b) * 100, ".3f") # 비율 구하는 공식
    print(str(result) + '%')
    # 초기화
    all = []
