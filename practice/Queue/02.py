# Queue 알고리즘 프로그램

class Queue():
    
    # 큐 생성
    def __init__(self):
        self.queue = []

    # 생성된 큐에 값 추가
    def enqueue(self, data):
        self.queue.append(data)

    # 생성된 큐에 담겨있는 값 제거
    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:]

        return dequeue_object

    # 생성된 큐에 담겨있는 가장 맨 앞에 있는 값이 어떤 값인지 알려줌
    def peek(self):
        peek_object = None # 초기화
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.queue[0]

        return peek_object

    def rear(self):
        rear_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            # 만약 큐가 비어있지 않다면
            # 큐 속의 값이 3개 이상일 때부터 카운트 시작
            if (len(self.queue) > 2) :
                length = len(self.queue)
                rear_object = self.queue[length - 1]
            else:
                rear_object = 0

        return rear_object

    # 생성된 큐가 현재 비어있는지 확인해줌
    def isEmpty(self):
        is_empty = False # is_empty 변수의 초기값을 False로 지정해놨기 때문에 else문을 굳이 쓰지 않아도 됨
        if len(self.queue) == 0:
            is_empty = True
        return is_empty

    # 종료 함수
    def finish(self):
        exit()

    # 큐 실행
    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    lq = Queue()
    while (1): # 무한루프
        select = input('[ 추가 : A / 삭제 : B / 종료 : C ] 중 무엇을 실행할까요? ')
        if (select == 'A'):
            data = input('추가 할 값을 입력하세요 : ')
            lq.enqueue(data)
            lq.printQueue()
            print('{}, {}'.format(lq.peek(), lq.rear()))
        elif (select == 'B'):
            lq.dequeue()
            lq.printQueue()
            print('{}, {}'.format(lq.peek(), lq.rear()))
        else:
            print('Queue 프로그램을 종료합니다.')
            lq.finish()