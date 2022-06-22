import time

def up_to_down(arr):
    result = 0
    # solve here
    arr = sorted(arr[1:], reverse=1)

    return arr


def answer_up_to_down():
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(up_to_down([3, 15, 27, 12]))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_up_to_down())
    print(f"{time.time() - start:.10f} sec")


