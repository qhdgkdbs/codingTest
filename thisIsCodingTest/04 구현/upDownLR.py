import time

def up_down_lr(n, data):
    # 11 12 13
    # 21 22 23
    # 31 32 33
    now = [1, 1]

    for move in data:
        if move == 'U':
            now[0] -= 1
            if now[0] == 0:
                now[0] += 1
        elif move == 'D':
            now[0] += 1
            if now[0] == n:
                now[0] += 1
        elif move == 'L':
            now[1] -= 1
            if now[1] == 0:
                now[1] += 1
        elif move == 'R':
            now[1] += 1
            if now[1] == n:
                now[1] -= 1
        else:
            print("input err")

    return now


def answer_up_down_lr(n, plans):
    x, y = 1, 1

    # L R U D 에 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    return x, y


if __name__ == '__main__':
    start = time.time()
    print(up_down_lr(5, ['R', 'R', 'R', 'U', 'D', 'D']))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_up_down_lr(5, ['R', 'R', 'R', 'U', 'D', 'D']))
    print(f"{time.time() - start:.10f} sec")


