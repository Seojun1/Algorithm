print('a부터 b까지의 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))
all = []

for i in range(a, b + 1):
    all.append(i)

print('{0}부터 {1}까지 정수의 합은 {2}입니다.'.format(a, b, sum(all)))