def dfs(graph, start, visited):
    # 현재 노드 방문처리
    visited[start] = True
    print(start, end =' ')

    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)


if __name__ == '__main__':
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

    visited = [False] * len(graph)

    dfs(graph, 1, visited)
