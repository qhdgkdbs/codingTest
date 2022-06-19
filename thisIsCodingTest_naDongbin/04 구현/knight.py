import time


def check_valid(nx, ny):
    if ny > 0 and nx > 0:
        return 1
    else:
        return 0


def knight(loc):
    result = 0
    # solve here
    a_to_num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x, y = a_to_num.index(loc[0]) + 1, int(loc[1])

    # [x x 0 x 0 x x]
    ny = y - 2
    nx = x - 1
    if check_valid(nx, ny):
        result += 1
    nx = x + 1
    if check_valid(nx, ny):
        result += 1
    # [x 0 x x x 0 x]
    ny = y - 1
    nx = x - 2
    if check_valid(nx, ny):
        result += 1
    nx = x + 2
    if check_valid(nx, ny):
        result += 1
    # [x x x O x x x]
    # [x 0 x x x 0 x]
    ny = y + 1
    nx = x - 2
    if check_valid(nx, ny):
        result += 1
    nx = x + 2
    if check_valid(nx, ny):
        result += 1
    # [x x 0 x 0 x x]
    ny = y + 2
    nx = x - 1
    if check_valid(nx, ny):
        result += 1
    nx = x + 1
    if check_valid(nx, ny):
        result += 1

    # print(x, y)

    return result


def answer_knight(loc):
    row = int(loc[1])
    col = int(ord(loc[0])) - int(ord('a')) + 1

    steps = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, -2), (1, 2)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]

        if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <= 8:
            result += 1

    return result


if __name__ == '__main__':
    start = time.time()
    print(knight('a1'))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_knight('a1'))
    print(f"{time.time() - start:.10f} sec")


