n = int(input())

tile = [[1, 2], [2, 1], [2, 2]]

# 가로가 N 일때 바닥을 채울 수 있는 경우의 수
arr = [0] * (n+1)
arr[1] = 1
arr[2] = 3

# arr[i] = arr[i-1] + 1 + arr[i-2] + 3
for i in range(3, n + 1):
    arr[i] = (arr[i - 1] * 1) + (arr[i - 2] * 2)

print(arr[n] % 796796)