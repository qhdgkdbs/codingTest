import sys

a = int(input())
for _ in range(0, a):
    i, j = list(map(int, sys.stdin.readline().rstrip().split()))
    print(i+j)