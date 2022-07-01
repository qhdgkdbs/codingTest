n, m = 4, 4
# 1 3 1 5
# 2 2 4 1
# 5 0 2 3
# 0 6 1 2
arr = [[1,2,5,0], [3,2,0,6], [1,4,2,1], [5,1,3,2]]
dp = [[0] * len(arr[0]) for _ in range(len(arr))]

dp[0] = arr[0]

for row in range(1, len(arr)):
    for cell in range(len(arr[0])):
        # row는 체크 안해도 됨.
        # 위 row의 왼쪽에서 오는 경우
        if cell - 1 < 0: up_left = 0
        else: up_left = dp[row-1][cell - 1]

        # 위 row에서 오는 경우
        up = dp[row-1][cell]

        # 위 row의 오른쪽에서 오는 경우
        if cell + 1 >= len(arr[0]): up_right = 0
        else: up_right = dp[row-1][cell + 1]

        dp[row][cell] = arr[row][cell] +  max(up, up_right, up_left)

print(dp)
