'''
4 6
9 15 10 17
'''

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    last_h = 0


    while start <= end:
        mid = (start + end) // 2

        len_rice = 0
        for i in arr:
            len_rice += (i - arr[mid]) if (i - arr[mid] > 0) else 0

        if len_rice == target:
            return arr[mid]

        # 잘라진 떡의 사이즈가 짧은 경우
        if len_rice < target:
            end = mid - 1
            last_h = arr[mid]
        # 잘라진 떡의 사이즈가 더 커
        elif len_rice > target:
            start = mid + 1
            last_h = arr[mid]

    return last_h


arr.sort()
print(binary_search(arr, m, 0, len(arr)-1))