# 위치 알려주기
# 첫번째 방법 (find 사용)
a = "Python is the best choice"
print(a.find('b')) # 문자열에서 b가 처음 나온 위치
print(a.find('k')) # 문자열에서 K가 존재하지 않다면 -1 출력

# 두번째 방법 (index 사용)
a = "Life is too short"
print(a.index('t')) # 문자열에서 t가 처음 나온 위치 / 존재하지 않다면 오류 뜸