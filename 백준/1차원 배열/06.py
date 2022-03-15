N = int(input())
yes = []
cnt = 0

# 환경구축
for i in range(N):
    quiz = input()
    # 입력 값을 a라는 리스트에 한 단어씩 추가
    a = list(quiz)
    # 탐색 시작
    for i in a:
        if i == 'O':
            cnt += 1
            yes.append(cnt)
        else:
            cnt = 0
    # result
    print(sum(yes))
    # 초기화
    cnt = 0
    yes = []