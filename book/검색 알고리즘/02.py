from typing import Sequence, Any

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []

def seq_search(a:Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i    # 검색성공 (인덱스 반환)
    return -1   # 검색실패 (-1을 반환)

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input('검색할 값을 입력하세요 : '))

idx = seq_search(x, ky)
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')