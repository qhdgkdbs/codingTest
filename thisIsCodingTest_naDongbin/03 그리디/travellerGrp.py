def traveller_grp(n, data):
    data.sort()
    count = 0
    grp = 0

    for min_cnt in data:
        count += 1

        if count >= min_cnt:
            grp += 1
            count = 0

    return count


if __name__ == '__main__':
    print(traveller_grp(5, [2, 3, 1, 2, 2]))


