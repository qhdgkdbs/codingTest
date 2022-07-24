from collections import deque

def bfs(graph, start, visited):
    # 첫 노드에서 방문할 수 있는 모든 노드 큐에 넣어
    queue = deque([start])

    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 현 노드와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

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
    bfs(graph, 1, visited)