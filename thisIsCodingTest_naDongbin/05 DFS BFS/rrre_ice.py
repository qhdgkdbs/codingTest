import sys
input = sys.stdin.readline
# 세로 가로
n, m = list(map(int, input().split()))

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def dfs(i, j):
    if i <= -1 or j <= -1 or i >= n or j >= m:
        return False

    if arr[i][j] == 0:
        arr[i][j] = 1
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            answer += 1

print(answer)


