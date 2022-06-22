import time
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


def func_name(size, data):
    result = 0
    # solve here
    global graph, n, m
    n, m = list(map(int, size.split()))
    graph= [list(map(int, row.split())) for row in data.split('/')]

    global dx, dy
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    return bfs(0, 0)


def answer_():
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(func_name('5 6', '1 0 1 0 1 0/1 1 1 1 1 1/0 0 0 0 0 1/1 1 1 1 1 1/1 1 1 1 1 1'))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_())
    print(f"{time.time() - start:.10f} sec")


