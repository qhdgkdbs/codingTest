import time


def ins_sort(arr):
    # i -> min IDX
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    start = time.time()
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    ins_sort(arr)
    print(arr)
    print(f"{time.time() - start:.10f} sec")

