# 입력
import sys
N = int(sys.stdin.readline())
X = set(map(int, sys.stdin.readline().split()))	# 탐색 시간을 줄이기 위해 set 사용
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for num in arr:				# arr의 원소를 하나씩 꺼내서 탐색함
    print(1) if num in X else print(0)	# num이 X 안에 있으면 1, 없으면 0 출력
