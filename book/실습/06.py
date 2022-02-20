# 숫자의 총합 구하기
N = input()
num = N.split(',')
int(num)
print(num)
cnt = 0

for i in num:
    cnt += int(i)

print(cnt)