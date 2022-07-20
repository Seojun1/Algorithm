def bubble_sort(data):
    print('[original list] :', data)
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                print(data)

arr = []
for e in range(5):
    arr.append(int(input(f'리스트 값을 지정하세요 ({e + 1}/5) : ')))

bubble_sort(arr)
print('[final list] : ', arr)