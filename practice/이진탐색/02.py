# binary_search
# data 중에서 target 을 검색하여 index 값을 return 한다.
# 없으면 None을 return한다.

def binary_serach(data, target):
    data.sort() # 오름차순으로 정리해놔야 이분탐색이 가능함
    left = 0
    right = len(data) -1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

# 테스트용 코드
if __name__ == '__main__':
    li = []
    for i in range(5):
        li.append(int(input(f'{i + 1}개의 리스트의 값을 입력하세요 : ')))
    target = 9
    idx = binary_serach(li, target)

    if idx:
        print(li[idx])
    else:
        print(f"찾으시는 타겟 {target}가 없습니다.")