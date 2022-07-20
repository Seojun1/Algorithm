def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        print(data)

arr = [3, 1, 2, 5, 4]
# 정렬한 배열을 출력
selection_sort(arr)
print("[Sorted array]")
print(arr)