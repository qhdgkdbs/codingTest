'''
10 7
1 3 5 7 9 11 13 15 17 19
'''

def binary_s(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None


size, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

print(binary_s(arr, target, 0, size-1) + 1)