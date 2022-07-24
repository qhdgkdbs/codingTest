import time

def find_parts(stock, s_item, req, r_item):
    ##################################
    # answer_find_parts 가 훨씬 빠름... #
    ##################################
    # solve here
    r_item = list(map(int, r_item.split()))
    s_item = list(map(int, s_item.split()))

    for i in r_item:
        if s_item.count(i):
            print('yes', end=' ')
        else:
            print('no', end=' ')


def answer_find_parts(stock, s_item, req, r_item):
    result = 0
    r_item = set(map(int, r_item.split()))
    s_item = set(map(int, s_item.split()))

    for i in r_item:
        if i in s_item:
            print('yes', end=' ')
        else:
            print('no', end=' ')


if __name__ == '__main__':
    start = time.time()
    find_parts(5, '8 3 7 9 2', 3, '5 7 9')
    print(f"\n{time.time() - start:.10f} sec")

    start = time.time()
    answer_find_parts(5, '8 3 7 9 2', 3, '5 7 9')
    print(f"\n{time.time() - start:.10f} sec")


