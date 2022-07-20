N = int(input())
word = []
for i in range(N):
    word.append(input())
# 중복 삭제
set_word = list(set(word))

# 정렬된 값을 넣어놓을 리스트 선언
sort_word = []
for i in set_word:
    sort_word.append((len(i), i))
sort_word = sorted(sort_word)

for len_word, word in sort_word:
    print(word)