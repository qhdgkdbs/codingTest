# 다익스트라
# start 에서 갈 수 있는 모든 경우를 파악
# distance 중 INF가 아닌 값의 수, INF가 아닌 값이 아닌 최대값 를 리턴

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 도시의 수, 간선의 수, start
n, m, s_node = list(map(int, input().split()))

# 각 노드별로 연결된 간선 정보
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))

distance = [INF] * (n+1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    # 이따가 카운팅 할떄 이거 참고 해야함.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리가 돤 경우
        if dist > distance[now]:
            continue

        # 연결된 노드의 정보
        for i in graph[now]:
            # i[0]: to node, i[1]: v to i[o] cost
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


count = 0
time = 0

dijkstra(s_node)

for i in distance:
    if i != INF and i != 0:
        count += 1
        if time < i: time = i

print(count, time)


# 3 2 1
# 1 2 4
# 1 3 2
