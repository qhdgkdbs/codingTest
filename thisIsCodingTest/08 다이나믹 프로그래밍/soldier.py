# https://youtu.be/5Lu34WIx2Us?t=3622
# 최장 증가 부분 수열 (LIS)

arr = [4, 2, 5, 8, 4, 11 ,15]
l_arr = [1] * len(arr)

for i in range(len(arr)):
    for j in range(1, i):
        if arr[j] < arr[i]:
            l_arr[i] = max(l_arr[i], l_arr[j]+1)

print(len(arr) - max(l_arr))