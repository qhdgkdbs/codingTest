import time


def next_loc(x, y, d, size, data):
    # 왼쪽 순서로 회전 북 서 남 동
    data[y][x] = 2

    loop_cnt = 1
    while loop_cnt <= 4:
        # nx와 ny 활용
        nx, ny = x, y
        # x y
        # 북 서 남 동
        # 0 -> -1 0
        # 1 -> 0 -1
        # 2 -> 1 0
        # 3 -> 1 0

        if d == 0: nx = x - 1
        elif d == 3: ny = y + 1
        elif d == 2: nx = x + 1
        elif d == 1: ny = y - 1

        # if nx < 0 or nx >= size[0] or ny < 0 or ny >= size[1] or data[ny][nx]-> 다시 되돌려; else x = nx, y = ny
        if nx < 0 or nx >= size[0] or ny < 0 or ny >= size[1] or data[ny][nx] != 0:
            if d == 0: d = 3
            elif d == 3: d = 2
            elif d == 2: d = 1
            elif d == 1: d = 0

            loop_cnt += 1
            continue
        else:
            x, y = nx, ny
            return x, y

    # if 0 -> return
    # else -> if count = 4 -> return null; else 회전
    return -1, -1


def game(size, now, data):
    result = 1
    # solve here
    x = now[0]
    y = now[1]

    while 1:
        x, y = next_loc(x, y, now[2], size, data)
        if x == -1:
            break
        result += 1

    return result

###############################################################


def answer_game(size, now, data):
    n, m = size
    d = [[0] * m for _ in range(n)]
    x, y = now[0], now[1]
    direction = now[2]
    d[x][y] = 1

    array = data
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 1
    turn_time = 0
    while 1:
        direction -= 1
        if direction == -1:
            direction = 3

        nx = x + dx[direction]
        ny = y + dy[direction]

        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dx[direction]

            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    return count


if __name__ == '__main__':
    start = time.time()
    print(game([4, 4], [1, 1, 0], [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_game([4, 4], [1, 1, 0], [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]))
    print(f"{time.time() - start:.10f} sec")


