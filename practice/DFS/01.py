def dfs(graph, start_node) :
    visit = list()  # 방문했던 노드의 목록으 차례대로 저장할 리스트
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
            # append --> ['Tick', 'Tock', ['Ping', 'Pong']]
            # extend --> ['Tick', 'Tock', 'Ping', 'Pong']

    return visit

if __name__ == '__main__':
    # 그래프 구성
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

print(f"그래프를 통한 깊이우선탐색(DFS)결과 : {dfs(graph, 'A')}")