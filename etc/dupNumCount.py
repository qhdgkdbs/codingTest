def dup_num_count(arr):
    count = []
    set_arr = set(arr)
    for i in set_arr:
        cnt = arr.count(i)
        if cnt != 1:
            count.append(cnt)

    if not count:
        print("-1")
    print(count)


if __name__ == '__main__':
    arr = [3, 2, 4]
    dup_num_count(arr)