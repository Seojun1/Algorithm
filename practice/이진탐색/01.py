# 리스트에서 특정 숫자 위치 찾기(이분 탐색)
# 입력: 리스트 a, 찾는 값 x
# 출력: 찾으면 그 값의 위치, 찾지 못하면 -1
import sys

def binary_search(a, x):
    # 탐색할 범위를 저장하는 변수 start, end
    # 리스트 전체를 범위로 탐색 시작(0 ~ len(a)-1)
    start = 0
    end = len(a) - 1

    while start <= end: # 탐색할 범위가 남아 있는 동안 반복
        mid = (start + end) // 2  # 탐색 범위의 중간 위치
        if x == a[mid]:   # 발견!
            return mid
        elif x > a[mid]:  # 찾는 값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
            start = mid + 1
        else:             # 찾는 값이 더 작으면 왼쪽으로 범위를 좁혀 계속 탐색
            end = mid - 1

    return -1  # 찾지 못했을 때


if __name__ == '__main__':

    d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print('찾고자 하는 target의 값을 입력하세요.')
    t = int(sys.stdin.readline())
    if binary_search(d, t) == -1:
        print('탐색 실패')
    else:
        print(f'x[{binary_search(d, t)}]번째에 존재합니다.')