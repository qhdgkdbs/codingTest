# https://programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def func_cmp(x, y):
    a = str(x)
    b = str(y)

    t1 = int(a + b)
    t2 = int(b + a)

    return 1 if t1 - t2 >= 0 else -1


def solution(numbers):
    answer = []

    numbers = sorted(numbers, key=cmp_to_key(func_cmp), reverse=True)

    numbers = ''.join(map(str, numbers))

    return str(int(numbers))