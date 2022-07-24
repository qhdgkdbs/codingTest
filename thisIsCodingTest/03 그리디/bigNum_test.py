import time

def func_name(n, m, k, arr):
    result = 0

    arr.sort(reverse=1)
    max_arr = arr[0]
    sec_arr = arr[1]

    is_max = True
    # K번을 연속으로 더할 수 있음.
    for count in range(1, m+1):

        print(f'count:{count}, is_max:{is_max}, result:{result}')
        # 0 1 2 3...
        if count % k != 0:
            result += max_arr
        else:
            result += sec_arr

    return result


def answer_():
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(func_name(5,8,3, [2,4,5,4,6]))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_())
    print(f"{time.time() - start:.10f} sec")


