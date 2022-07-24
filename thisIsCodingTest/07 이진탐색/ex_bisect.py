from bisect import bisect_right, bisect_left


def func1():
    a = [1, 2, 4, 4, 8]
    x = 4

    print(f'func1 L:{bisect_left(a, x)}')
    print(f'func1 R:{bisect_right(a, x)}')

def count_by_range(a, l, r):
    r = bisect_right(a, r)
    l = bisect_right(a, l)
    return r - l

def func2():
    a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

    # 값인 4인 데이터의 개수 출력
    print(f'func2 find 4 ||       {count_by_range(a, 4, 4)}')
    # 값의 범위가 -1 ~ 3인 데이터의 개수 출력
    print(f'func2 find -1 ~ 3 ||  {count_by_range(a, -1, 3)}')


if __name__ == '__main__':
    func1()
    func2()


