# 정답 아님 이따 다시 푸셈


import time

def func_name():
    now, to = list(map(int, input().split()))
    result = 0
    # solve here
    # 7 34
    # 7 -> 17 27 32 33 34
    up = True
    if now > to: up = False

    while 1:
        tmp = abs(now - to)
        # 온도를 올려야하는 상황이고, 그 차이가 10이상이라면
        if tmp >= 10:
            if up: now += 10
            else: now -= 10
            result+=1
        elif tmp >=5:
            if up:now += 5
            else:now -= 5
            result += 1
        elif tmp >= 1 :
            if up: now += 1
            else: now -= 1
            result += 1
        else:
            break

    return result


def answer_():
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(func_name())
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_())
    print(f"{time.time() - start:.10f} sec")


