def linear_serach(arr, target):
    n = len(arr)
    for i in range(n):
        if target == arr[i]:
            return i
    return None

nums = [1, 2, 3, 4, 5, 6, 7]
x = 8
lim = linear_serach(nums, x)
print(f'x[{lim}] 위치에 존재합니다.')