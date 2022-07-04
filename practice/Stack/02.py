# 클래스 선언
class Stack:

    # stack의 기본적인 리스트 생성
    def __init__(self):
        self.stack = []
    # stack이라는 박스안에 값 추가.
    def push(self, data):
        self.stack.append(data)
    # stack안에 담겨있는 값을 하나씩 꺼낸다.
    def pop(self):
        if len(self.stack) <= 0:
            return ("No Data in Stack")
        else:
            return self.stack.pop()

ExStack = Stack()
ExStack.push("A")
ExStack.push("B")
ExStack.push("C")
ExStack.push("D")

ExStack.pop()
ExStack.pop()
print(ExStack.stack)