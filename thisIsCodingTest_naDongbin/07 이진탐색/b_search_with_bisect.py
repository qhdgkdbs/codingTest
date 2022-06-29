from bisect import bisect_right, bisect_left
'''
10 7
1 3 5 7 9 11 13 15 17 19
'''

size, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

print(bisect_left(arr, target) + 1)