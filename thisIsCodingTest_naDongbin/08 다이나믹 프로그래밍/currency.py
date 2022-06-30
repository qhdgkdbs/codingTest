'''
2 15
2 3
'''
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
cur = list(map(int, input().split()))

# 작은 것 부터 올라가자
arr = [10001] * (m + 1)
for i in range(min(cur)):
    arr[i] = -1
for i in cur:
    if i < n:
        arr[i] = 1


for i in range(max(cur), m + 1):
    # 가지고 있는 화폐 만큼 빼버린 것에 + 1
    for c in cur:
        if arr[i-c] != -1:
            arr[i] = min(arr[i], arr[i-c]+1)

# print(arr)

print(arr[m] if arr[m] != 10001 else -1)