INF = int(1e9)

# 회사의 수, 경로의 수
n, m = list(map(int, input().split()))

graph = [[INF] * (n+1) for _ in range(n+1)]

# 연결된 회사의 경로 | 가는거 오는거 대칭 and cost 1
for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a][b] = 1
    graph[b][a] = 1

last, mid = list(map(int, input().split()))

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0


for k in range(1, n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print((graph[1][mid] + graph[mid][last]) if graph[1][mid] != INF and graph[mid][last] != INF else -1)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
