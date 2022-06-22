import time

def ch_Arr(max, arr1, arr2):
    result = 0
    # solve here
    # 두 배열을 합치고 상위 5개로 배열을 하나 뽑아
    # 그리고 for max: newArr 큰거부터 가져와 -> 새로운 배열에 없으면 arr1의 제일 작은거랑 바꿔
    # print([y for x in [arr1, arr2] for y in x])
    # print(arr1 + arr2)
    # print([*arr1, *arr2])

    nArr = sorted([*arr1, *arr2], reverse=1)[:len(arr1)]
    arr1.sort(reverse=1)
    print(arr1)
    for idx in range(max):
        if nArr[idx] not in arr1:
            arr1[len(arr1) - idx - 1] = nArr[idx]

    print(arr1)
    return sum(arr1)


def answer_ch_Arr(max, arr1, arr2):
    result = 0
    # answer here
    arr1.sort()
    arr2.sort(reverse=1)

    for i in range(max):
        if arr1[i] < arr2[i]:
            arr1[i] = arr2[i]
        else:
            break

    return sum(arr1)


if __name__ == '__main__':
    start = time.time()
    arr1 = [1, 2, 5, 4, 3]
    arr2 = [5, 5, 6, 6, 5]
    print(ch_Arr(3, arr1, arr2))
    print(f"{time.time() - start:.10f} sec")

    start = time.time()
    arr1 = [1, 2, 5, 4, 3]
    arr2 = [5, 5, 6, 6, 5]
    print(answer_ch_Arr(3, arr1, arr2))
    print(f"{time.time() - start:.10f} sec")


