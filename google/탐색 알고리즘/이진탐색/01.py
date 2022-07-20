def binary_search(arr, target):
    left = 0
    right = len(arr) -1

    mid = (left+right) // 2
    while left <= right:
        if arr[mid] == target:
            return 1    # 탐색성공
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        if left > right:
            break

    return -1   # 탐색 실패

if __name__ == '__main__':
    arr_list = []
    N = int(input('몇개의 원소를 추가? '))
    for i in range(N):
        arr_list.append(int(input(f'x[{i}]번째 : ')))

    x = int(input('찾고자하는 target은?'))
    idx = binary_search(arr_list, x)

    if idx == 1:
        print(f'탐색성공. x[{arr_list.index(x)}]에 위치해있습니다.')
    else:
        print('탐색실패.')