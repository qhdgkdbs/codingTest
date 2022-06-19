def to_be_one(n, k):
    cnt = 0
    while n != 1:
        if n % k:
            cnt += 1
            n -= 1
        else:
            cnt += 1
            n //= k  #몫만 가져옴

    return cnt


if __name__ == '__main__':
    print(to_be_one(25, 3))
