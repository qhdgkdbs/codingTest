def min_change_num(n):
    coin_type = [500, 100, 50, 10]
    cnt = 0

    for coin in coin_type:
        cnt += n // coin
        n -= (n // coin)*coin  # -> n %= coin

    print(cnt)


if __name__ == '__main__':
    min_change_num(1260)