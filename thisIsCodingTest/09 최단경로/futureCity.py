import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

company, root = list(map(int, input().split()))

graph = [[] for _ in range(company + 1)]

for i in range(root):
    a, b = list(map(int, input().split()))
    graph[a].append((b, 1))
    graph[b].append((a, 1))

last, mid = list(map(int, input().split()))

distance = [INF] * (company + 1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        # 이미 처리가 된 경우
        if dist > distance[node]:
            continue

        for i in graph[node]:
            # dist, node 를 통해서 가는 방법
            # dist + node에서 i 로 가는 법
            cost = dist + 1
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)
to_mid = distance[mid]

distance = [INF] * (company + 1)

dijkstra(mid)
to_last = distance[last]


print((to_mid + to_last) if to_mid != INF and to_last != INF else -1)


# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

