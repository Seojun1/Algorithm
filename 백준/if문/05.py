# ěëěęł

H, M = map(int, input().split(' '))

if (H < 0 and M < 45):
    H = 23 - H
    M = 60 + (M - 45)
    print(H, M)
elif H > 0 and M >= 45:
    H -= 1
    M = 60 + (M - 45)
    print(H, M)
else:
    H -= 1
    M = 60 + (M - 45)
    print(H, M)