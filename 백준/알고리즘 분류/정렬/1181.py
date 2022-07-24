N = int(input())
a = []
for i in range(N):
    a.append(input())

# 중복의 문자열을 없애기 위해 사용(합집합)
a = list(set(a))
result = []
for j in a:
    result.append([len(j), j])

result = sorted(result)
for i in range(len(result)):
    print(result[i][1])