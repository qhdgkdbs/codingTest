import time

def mul_or_add(n):
    result = 0
    if int(n[0]) in [0, 1] or int(n[1]) in [0, 1]:
        result = int(n[0]) + int(n[1])
    else:
        result = int(n[0]) * int(n[1])

    for i in n[2:]:
        if i == 0 or i == 1:
            result += int(i)
        else:
            result *= int(i)

    return result


def answer_mul_or_add(n):
    result = int(n[0])

    for i in range(1, len(n)):
        num = int(n[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

    return result


if __name__ == '__main__':
    start = time.time()
    print(mul_or_add("02984"))
    print(mul_or_add("567"))
    print("time :", time.time() - start)

    start = time.time()
    print(answer_mul_or_add("02984"))
    print(answer_mul_or_add("567"))
    print("time :", time.time() - start)


