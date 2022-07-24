import time

def func_name():
    result = 0
    # solve here
    arr = []
    n, m = list(map(int, input().split()))

    for _ in range(n):
        arr.append(list(map(int, input().split())))


    min_arr_row = []
    for i in range(0, n):
        min_arr_row.append(min(arr[i]))

    return max(min_arr_row)


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


