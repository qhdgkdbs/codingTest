import time

def grade_low_top(data):
    result = 0
    # solve here
    r = [row.split() for row in data.split('/')]
    del r[0]

    n = sorted(r, key=lambda x: int(x[1]))

    name = [row[0] for row in n]

    return name


def answer_grade_low_top(data):
    result = 0
    # answer here

    return result


if __name__ == '__main__':
    start = time.time()
    print(grade_low_top('2/홍길동 95/이순신 77'))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_grade_low_top('2/홍길동 95/이순신 77'))
    print(f"{time.time() - start:.10f} sec")


