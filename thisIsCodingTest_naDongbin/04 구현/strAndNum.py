import time

def str_and_num(data):
    result = 0
    # solve here
    word = []
    num = 0

    for i in data:
        if ord(i) >= ord(str(0)) and ord(i) <= ord(str(9)):
            num += int(i)
        else:
            word.append(i)

    word.sort()
    result = ''.join(word) + str(num)

    return result


def answer_str_and_num(data):
    result = []
    value = 0

    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)

    result.sort()

    if value != 0:
        result.append(str(value))

    return ''.join(result)


if __name__ == '__main__':
    start = time.time()
    print(str_and_num('K1KA5CB7'))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    print(answer_str_and_num('K1KA5CB7'))
    print(f"{time.time() - start:.10f} sec")


