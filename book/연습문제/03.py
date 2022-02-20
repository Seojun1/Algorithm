# 881120-1068234 <-- 주민등록번호를 연월일 부분(YYYYMMDD)과 그 뒤의 숫자 부분으로 나누어 출력하시오.

num = "881120-1068234"

yyyymmdd = num[:6]
num = num[7:]
print(yyyymmdd)
print(num)