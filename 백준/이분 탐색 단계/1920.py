from sys import stdin, stdout

n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = list(map(int, input().split()))

for i in range(len(M)):
    if (M[i] in N):
        print(1)
    else:
        print(0)


