num = 26
arr = [0] * 3001

for i in range(2, num + 1):
    # 1을 뺀 경우
    arr[i] = arr[i-1] + 1

    # N 으로 나누어지는 경우
    if arr[i] % 5 == 0:
        arr[i] = min(arr[i], arr[i // 5] + 1)
    if arr[i] % 3 == 0:
        arr[i] = min(arr[i], arr[i // 3] + 1)
    if arr[i] % 2 == 0:
        arr[i] = min(arr[i], arr[i // 2] + 1)


print(arr[num])