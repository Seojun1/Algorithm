# 더 간결하게
from typing import Sequence, Any


def seq_search(a:Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i    # 검색성공 (인덱스 반환)

    return -1   # 검색실패 (-1을 반환)


if __name__ == '__main__':
    list_a = []
    N = int(input('원소 수를 입력하세요 : '))
    for i in range(N):
        a = int(input(f'x[{i}] : '))
        list_a.append(a)

    search = int(input('검색할 값을 입력하세요 : '))

    idx = seq_search(list_a, search)

    if (idx == -1):
        print('검색 결과가 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
