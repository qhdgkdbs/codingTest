n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


# 세로 가로
def dfs(i, j):
    if i <= -1 or j <= -1 or i >= n or j >= m:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1

        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
        return True
    return False

result = 0
# 세로길이
for i in range(n):
    # 가로길이
    for j in range(m):
        # 세로, 가로
        if dfs(i, j) == True:
            result += 1

print(result)


