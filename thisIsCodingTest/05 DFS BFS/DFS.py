def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 - 2차원 리스트
# 그래프의 1번 노드가 시작하는 것을 맞추기 위해서 0번 인덱스를 []로 하고 1번 인덱스부터 사용
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# 정의 된 DFS 함수 호출
if __name__ == '__main__':
    dfs(graph, 1, visited)

