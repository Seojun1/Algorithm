# 리스트 정렬
# 1. sort() --> 리스트의 요소를 순서대로 정렬.
a = [1, 4, 3, 2]
a.sort()
print(a)

# 2. sort() --> 리스트의 알파벳을 순서대로 정렬.
a = ['a', 'c', 'b']
a.sort()
print(a)

# 3. reverse() --> 리스트를 역순으로 뒤집기.
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 4. index() --> 리스트에 x 값이 있으면 x의 위치 값을 돌려줌. ( 값이 없으면 오류 발생. )
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))