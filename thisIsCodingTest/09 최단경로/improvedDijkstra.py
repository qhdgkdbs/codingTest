import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 간선
n, m = list(map(int, input().split()))

start = int(input())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n+1)

# 모든 간선의 정보 받기
for _ in range(m):
    node, to, weight = list(map(int, input().split()))
    graph[node].append((to, weight))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, q_node = heapq.heappop(q)

        # 이미 처리가 된 경우
        if dist > distance[q_node]:
            continue

        # 현재 노드와 연결된 모든 노드 확인
        for i in graph[q_node]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print([i if i != INF else 'INF' for i in distance][1:])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2


