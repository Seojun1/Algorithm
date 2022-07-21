from sys import stdin
N = int(stdin.readline())
M = sorted(map(int, stdin.readline().split()))
N2 = int(stdin.readline())
M2 = list(map(int, stdin.readline().split()))

for i in range(len(M2)):
    if M2[i] in M:
        print(1)
    else:
        print(0)