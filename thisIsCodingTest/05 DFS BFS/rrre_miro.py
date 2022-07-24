import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

queue = deque([])
queue.append((0,0))
while queue:
    i, j = queue.popleft()

    for move in range(4):
        ni = i + di[move]
        nj = j + dj[move]
        # 범위 밖
        if ni <= -1 or nj <= -1 or ni >= n or nj >= m:
            continue

        # 가는 곳에 괴물
        if arr[ni][nj] == 0:
            continue

        # 첫 방문인 경우
        if arr[ni][nj] == 1:
            arr[ni][nj] = arr[i][j] + 1
            queue.append((ni, nj))

print(arr[n-1][m-1])


'''
5 6
1 0 1 0 1 0
1 1 1 1 1 1
0 0 0 0 0 1
1 1 1 1 1 1
1 1 1 1 1 1
'''