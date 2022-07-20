# import sys
#
# def selection_sort(data):
#     for i in range(len(data)):
#         min_data = i
#         for j in range(i+1, len(data)):
#             if data[j] < data[min_data]:
#                 min_data = j
#         data[i], data[min_data] = data[min_data], data[i]
#
# N = int(sys.stdin.readline())
# arr = []
# for i in range(N):
#     arr.append(int(sys.stdin.readline()))
#     arr.sort()
# selection_sort(arr)
# for j in arr:
#     print(j)


# 아니 선택정렬 문제라면서 왜 선택정렬 방식대로 코드를 짜면 시간초과가 나오는거지
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 결국엔 그냥 sort 함수 하나만 쓰면 풀리는 문제였구나.......
# 이럴거면 선택정렬이라고 하질 말던가
# 와 선택정렬 문제 뿐만아니라 버블정렬, 삽입정렬 문제에도 밑에 있는 이 코드가 해당이 되는거였네
# C++로 알고리즘 공부할걸 그랬나 너무 헷갈린다 흑
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

a.sort()

for j in a:
    print(j)