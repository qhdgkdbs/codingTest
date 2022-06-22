import time

def get_count(n, find, array):
    result = 0
    # solve here
    start = 0
    end = len(array) - 1
    is_it = 0

    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == find:
            is_it = 1
            break
        elif array[mid] > find:
            end = mid - 1
        else:
            start = mid + 1

    if not is_it:
        return -1

    # mid -> find 값
    # 앞으로 쭉가고, 뒤로 쭉가보자
    idx = mid
    # 마이너스 해보자
    while find == array[idx]:
        result += 1
        idx -= 1
    idx = mid + 1
    while find == array[idx]:
        result += 1
        idx += 1

    return result


def answer_get_count():
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(get_count(7, 9, [1, 1, 2, 2, 2, 2, 3]))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_get_count())
    print(f"{time.time() - start:.10f} sec")


