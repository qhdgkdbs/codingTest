import time

# 최대 rec 깊이 조절
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)


def fibo(x):
    print(x)
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


def fibo_with_d_rec(x):
    d = [0] * 150
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    return fibo_with_d_rec(x-1) + fibo_with_d_rec(x-2)

def fibo_with_d_rep(x):
    d = [0] * 150

    d[1] = d[2] = 1

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]


if __name__ == '__main__':
    start = time.time()
    print(fibo(10))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(fibo_with_d_rec(10))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(fibo_with_d_rep(10))
    print(f"{time.time() - start:.10f} sec")

