# print('+와 -를 번갈아 출력합니다.')
# a = int(input('몇개를 출력할까요? '))
# pm = '+-'
#
# a = a//2
# print(pm * a)

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇개를 출력할까요? '))

for i in range(n):
    if i % 2: # 홀수인 경우
        print('-', end='')
    else:   # 짝수인 경우
        print('+', end='')
print()