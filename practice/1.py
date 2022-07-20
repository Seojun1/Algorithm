# 오름차순

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array)

arr = [4, 6, 1, 7, 2, 9, 3]
print(f'[The original] : {arr}')
bubbleSort(arr)
print(f'[correction] : {arr}')