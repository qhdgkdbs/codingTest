import time

def func_name():
    result = 0
    # solve here
    num, k = list(map(int, input().split()))

    while 1:
        if num % k != 0:
            num -= 1
            result += 1
        else:
            num /= k
            result += 1

        if num == 1:
            return result
    return 0


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


