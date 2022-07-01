INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a][b] = c

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0
        if i == 0 or j == 0:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print([[graph[j][i] for i in range(1, len(graph))] for j in range(1, len(graph))])


# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
