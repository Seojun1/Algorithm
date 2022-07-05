b = []

def solution(data):
    for i in range(len(answer)):
        b.append(data[i])

    for i in range(2):
        b.remove(min(b))
    print(sum(b))

answer = [50, 150, 200, 100, 300, 200]
solution(answer)