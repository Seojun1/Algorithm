# 상수 ( 입력받은 숫자를 뒤집는 부분만 구글 참고 )
# 숫자 입력받기
a, b = map(int, input().split())

# 2개의 값을 넣기 위해 빈 리스트 생성
list = []

# 입력받은 숫자 뒤집기
c = int(str(a)[::-1])
d = int(str(b)[::-1])

# 뒤집은 값을 리스트에 대입 
list = c, d

# 대소비교
print(max(list))
