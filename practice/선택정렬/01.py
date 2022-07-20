def selection_sort(data):
    print('original list : ',data)
    # 리스트만큼 반복한다.
    for i in range(len(data)):
        # 가장 최소의 값을 저장할 변수 min_data 선언
        min_data = i

        #  data[1]부터 리스트의 끝에 도달할때까지 반복한다.
        for j in range(i + 1, len(data)):
            # 만약 data[j]가 data[min_data]보다 작다면
            if data[j] < data[min_data]:
                # 순서를 바꿈으로써 숫자들을 정렬한다.
                data[j], data[min_data] = data[min_data], data[j]
                print('sorting... ====> ', data)

arr = [3, 5, 1, 2, 8, 4]
selection_sort(arr)
print('final list : ',arr)