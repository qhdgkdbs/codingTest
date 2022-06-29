from collections import deque

# 세로, 가로
n, m = list(map(int, input().split()))

print(n,m)

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(graph)

def bfs(i, j):
    # 큐 활용시 일단 초기화 후 삽입하기
    queue = deque()
    queue.append((i,j))

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while queue:
        i, j = queue.popleft()

        for move in range(4):
            ni = i + di[move]
            nj = j + dj[move]

            # 범위 밖인 경우
            if ni <= -1 or nj <= -1 or ni >= n or nj >= m:
                continue

            # 괴물이 있는 경우
            if graph[ni][nj] == 0:
                continue

            # 첫 방문인 경우
            if graph[ni][nj] == 1:
                graph[ni][nj] = graph[i][j] + 1
                queue.append((ni, nj))

    return graph[n-1][m-1]


print(bfs(0, 0))