import time


def dfs(x, y):
    #     범위가 벗어나는 경우 탈주
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면,
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


def answer_ice(x, y, data):
    result = 0

    global n, m, graph
    # solve here
    # map(function, iterable) -> 배열 형태로 나온다 생각하자
    # 문자열.split() -> "띄어쓰기, 엔터"로 구별함
    # 문자열.split('구분자')
    # 문자열.split('구분자', 분할횟수)
    # 문자열.split(sep='구분자', maxsplit=분할횟수)
    graph = [list(map(int, row.split())) for row in data.split('/')]

    n, m = x, y

    for i in range(n):
        for j in range(m):
            # 현재 위치에서 조져
            if dfs(i, j) == True:
                result += 1

    return result


def answer_():
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(answer_ice(4, 5, '0 0 1 1 0/0 0 0 1 1/1 1 1 1 1/0 0 0 0 0'))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_())
    print(f"{time.time() - start:.10f} sec")


