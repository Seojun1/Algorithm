arr_list = []

def linear_search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return 1    # 탐색성공
    return -1   # 탐색실패

if __name__ == '__main__':
    N = int(input('몇개의 원소를 추가? '))
    for i in range(N):
        arr_list.append(int(input(f'x[{i}]번째 : ')))

    x = int(input('찾고자하는 target은?'))
    idx = linear_search(arr_list, x)

    if idx == 1:
        print(f'탐색성공. x[{arr_list.index(x)}]에 위치해있습니다.')
    else:
        print('탐색실패.')