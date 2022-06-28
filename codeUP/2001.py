import time

def func_name(price):
    # solve here
    p = min(price[:3])
    j = min(price[3:])

    return round((p+j)*1.1, 1)


def answer_():
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(func_name([800, 700, 900, 198, 330]))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_())
    print(f"{time.time() - start:.10f} sec")


