from sys import stdin

def binary_seach(data, target):
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


a, b = map(int, stdin.readline().split())
li1 = sorted([input() for _ in range(a)])
li2 = sorted([input() for _ in range(b)])

result = []
for i in li2:
    idx = binary_seach(li1, i)
    if idx == 1:
        result.append(i)
    else:
        pass

print(len(result))
for c in result:
    print(c)