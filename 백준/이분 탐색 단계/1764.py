def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left+right) // 2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

N, M = map(int, input().split())
li1 = sorted([input() for _ in range(N)])
li2 = sorted([input() for _ in range(M)])

result = []
for i in li2:
    idx = binary_search(li1, i)
    if idx == 1:
        result.append(i)
    else:
        pass
print(len(result))
for j in result:
    print(j)