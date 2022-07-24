# 세로 가로
n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(i, j):
    # 범위가 벗어난 경우
    if i <= -1 or j <= -1 or i >= n or j >= m:
        return False

    # 해당 좌표가 얼음인 경우
    if graph[i][j] == 0:
        graph[i][j] = 1

        # 사방 방문 깊게~
        for _ in range(4):
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)
