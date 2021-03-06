import time

def clock_count(n):
    time_sec = list(range(0, 60))

    count = 0

    for time in time_sec:
        for sec in time_sec:
            if '3' in str(time) or '3' in str(sec):
                count += 1
    # 싸이클 한번에 1575

    if n < 3:
        count *= (n + 1)
    elif n < 13:
        count *= n
        count += 3600
    elif n < 23:
        count *= (n - 1)
        count += 3600 * 2
    else:
        count *= (n - 2)
        count += 3600 * 3

    return count


def answer_clock_count(n):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count


if __name__ == '__main__':
    start = time.time()
    print(clock_count(24))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_clock_count(24))
    print(f"{time.time() - start:.10f} sec")


